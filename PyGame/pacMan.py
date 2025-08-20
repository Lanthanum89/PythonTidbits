import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SIZE = 30
DOT_SIZE = 10
GHOST_SIZE = 15
PLAYER_SPEED = 5
STARTING_LIVES = 3  # Number of lives

# Colours
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PINK = (255, 105, 180)
ORANGE = (255, 165, 0)
CYAN = (0, 255, 255)
GREEN = (0, 255, 0)
PURPLE = (153, 50, 204)
GOLD = (255, 215, 0)

# Add more ghost colors as needed
GHOST_COLORS = [RED, PINK, ORANGE, CYAN, GREEN, PURPLE, GOLD]
GHOST_SPEEDS = [1, 1.2, 0.8, 1.5, 1.7, 0.9, 1.3]  # Different speeds for each ghost

NUM_GHOSTS = len(GHOST_COLORS)

# Particle system for Pac-Man and ghosts
pacman_particles = []
ghost_particles = [ [] for _ in range(NUM_GHOSTS) ]  # One list per ghost

def add_particle(particles, x, y, color, size):
    particles.append({
        "x": x,
        "y": y,
        "radius": size,
        "color": color,
        "alpha": 128,  # Lower initial alpha for a subtler effect
        "dx": random.uniform(-0.3, 0.3),  # Smaller spread for a tighter trail
        "dy": random.uniform(-0.3, 0.3)
    })
    if len(particles) > 15:  # Fewer particles for a lighter effect
        particles.pop(0)

def update_particles(particles):
    for p in particles:
        p["x"] += p["dx"]
        p["y"] += p["dy"]
        p["alpha"] = max(0, p["alpha"] - 8)  # Fade a bit slower
        p["radius"] = max(1, p["radius"] - 0.1)  # Shrink more gently
    # Remove fully faded particles
    particles[:] = [p for p in particles if p["alpha"] > 0 and p["radius"] > 1]

def draw_particles(surface, particles):
    for p in particles:
        surf = pygame.Surface((int(p["radius"]*2), int(p["radius"]*2)), pygame.SRCALPHA)
        pygame.draw.circle(surf, p["color"] + (int(p["alpha"]),), (int(p["radius"]), int(p["radius"])), int(p["radius"]))
        surface.blit(surf, (p["x"] - p["radius"], p["y"] - p["radius"]))

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Pac-Man")
clock = pygame.time.Clock()

def reset_game():
    global player, player_direction, ghosts, dots, score, game_over, lives, pacman_particles, ghost_particles
    player = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, PLAYER_SIZE, PLAYER_SIZE)
    player_direction = 0
    ghosts = []
    min_dist = 200  # Minimum distance from Pac-Man at start
    for i in range(NUM_GHOSTS):
        while True:
            x = random.randint(0, SCREEN_WIDTH - GHOST_SIZE)
            y = random.randint(0, SCREEN_HEIGHT - GHOST_SIZE)
            ghost_rect = pygame.Rect(x, y, GHOST_SIZE, GHOST_SIZE)
            # Ensure ghost is far enough from Pac-Man's starting position
            dist = ((ghost_rect.centerx - player.centerx) ** 2 + (ghost_rect.centery - player.centery) ** 2) ** 0.5
            if dist >= min_dist:
                break
        color = GHOST_COLORS[i % len(GHOST_COLORS)]
        speed = GHOST_SPEEDS[i % len(GHOST_SPEEDS)]
        ghosts.append({"rect": ghost_rect, "dx": speed, "dy": speed, "color": color})
    dots = []
    for _ in range(20):
        x = random.randint(0, SCREEN_WIDTH - DOT_SIZE)
        y = random.randint(0, SCREEN_HEIGHT - DOT_SIZE)
        dot = pygame.Rect(x, y, DOT_SIZE, DOT_SIZE)
        dots.append(dot)
    score = 0
    game_over = False
    lives = STARTING_LIVES
    pacman_particles = []
    ghost_particles = [ [] for _ in range(NUM_GHOSTS) ]

def reset_player_position():
    global player, player_direction
    player = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, PLAYER_SIZE, PLAYER_SIZE)
    player_direction = 0

def draw_heart(surface, x, y, size, color):
    # Draw a simple heart shape using two circles and a triangle
    radius = size // 4
    # Left circle
    pygame.draw.circle(surface, color, (x + radius, y + radius), radius)
    # Right circle
    pygame.draw.circle(surface, color, (x + 3 * radius, y + radius), radius)
    # Bottom triangle
    points = [
        (x + radius // 2, y + radius + 2),
        (x + 3 * radius + radius // 2, y + radius + 2),
        (x + size // 2, y + size)
    ]
    pygame.draw.polygon(surface, color, points)

# Game variables
reset_game()
running = True

# Main game loop
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if game_over and event.key == pygame.K_SPACE:
                reset_game()

    if not game_over:
        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.x -= PLAYER_SPEED
            player_direction = 180
        if keys[pygame.K_RIGHT]:
            player.x += PLAYER_SPEED
            player_direction = 0
        if keys[pygame.K_UP]:
            player.y -= PLAYER_SPEED
            player_direction = 90
        if keys[pygame.K_DOWN]:
            player.y += PLAYER_SPEED
            player_direction = 270

        # Keep player on screen
        player.x = max(0, min(player.x, SCREEN_WIDTH - PLAYER_SIZE))
        player.y = max(0, min(player.y, SCREEN_HEIGHT - PLAYER_SIZE))

        # Add Pac-Man particle at current position
        add_particle(pacman_particles, player.centerx, player.centery, YELLOW, PLAYER_SIZE // 3)
        update_particles(pacman_particles)

        # Ghost movement and particles
        for idx, ghost in enumerate(ghosts):
            # Move towards player
            if ghost["rect"].x < player.x:
                ghost["rect"].x += ghost["dx"]
            else:
                ghost["rect"].x -= ghost["dx"]
            if ghost["rect"].y < player.y:
                ghost["rect"].y += ghost["dy"]
            else:
                ghost["rect"].y -= ghost["dy"]

            # Add ghost particle at current position
            add_particle(ghost_particles[idx], ghost["rect"].centerx, ghost["rect"].centery, ghost["color"], GHOST_SIZE // 2)
            update_particles(ghost_particles[idx])

            # Check ghost collision
            if player.colliderect(ghost["rect"]):
                lives -= 1
                if lives > 0:
                    reset_player_position()
                else:
                    game_over = True

        # Dot collection
        for dot in dots[:]:  # Use slice copy to safely remove while iterating
            if player.colliderect(dot):
                dots.remove(dot)
                score += 10

        # Win condition
        if not dots:
            game_over = True

    # Drawing
    screen.fill(BLACK)

    # Draw dots
    for dot in dots:
        pygame.draw.circle(screen, WHITE, (dot.centerx, dot.centery), DOT_SIZE // 2)

    # Draw ghost particles (behind ghosts)
    for plist in ghost_particles:
        draw_particles(screen, plist)

    # Draw Pac-Man particles (behind Pac-Man)
    draw_particles(screen, pacman_particles)

    # Draw ghosts (each with its own color)
    for ghost in ghosts:
        pygame.draw.rect(screen, ghost["color"], ghost["rect"])

    # Draw player (Pac-Man)
    pygame.draw.circle(screen, YELLOW, player.center, PLAYER_SIZE // 2)
    
    # Draw score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f'Score: {score}', True, WHITE)
    screen.blit(score_text, (10, 10))

    # Draw lives as red heart icons
    for i in range(lives):
        icon_x = 10 + i * (PLAYER_SIZE // 2 + 8)
        icon_y = 90
        draw_heart(screen, icon_x, icon_y, PLAYER_SIZE // 2, RED)

    # Game over text and restart option
    if game_over:
        if not dots:
            game_over_text = font.render('You Win!', True, WHITE)
        else:
            game_over_text = font.render('Game Over!', True, WHITE)
        text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20))
        screen.blit(game_over_text, text_rect)
        restart_text = font.render('Press SPACE to restart', True, WHITE)
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30))
        screen.blit(restart_text, restart_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
