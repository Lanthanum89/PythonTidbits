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
GHOST_SPEED = 1

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Pac-Man")
clock = pygame.time.Clock()

def reset_game():
    global player, player_direction, ghosts, dots, score, game_over
    player = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, PLAYER_SIZE, PLAYER_SIZE)
    player_direction = 0
    ghosts = []
    for _ in range(4):
        x = random.randint(0, SCREEN_WIDTH - GHOST_SIZE)
        y = random.randint(0, SCREEN_HEIGHT - GHOST_SIZE)
        ghost = pygame.Rect(x, y, GHOST_SIZE, GHOST_SIZE)
        ghosts.append({"rect": ghost, "dx": GHOST_SPEED, "dy": GHOST_SPEED})
    dots = []
    for _ in range(20):
        x = random.randint(0, SCREEN_WIDTH - DOT_SIZE)
        y = random.randint(0, SCREEN_HEIGHT - DOT_SIZE)
        dot = pygame.Rect(x, y, DOT_SIZE, DOT_SIZE)
        dots.append(dot)
    score = 0
    game_over = False

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

        # Ghost movement
        for ghost in ghosts:
            # Move towards player
            if ghost["rect"].x < player.x:
                ghost["rect"].x += ghost["dx"]
            else:
                ghost["rect"].x -= ghost["dx"]
            if ghost["rect"].y < player.y:
                ghost["rect"].y += ghost["dy"]
            else:
                ghost["rect"].y -= ghost["dy"]

            # Check ghost collision
            if player.colliderect(ghost["rect"]):
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

    # Draw ghosts
    for ghost in ghosts:
        pygame.draw.rect(screen, RED, ghost["rect"])

    # Draw player (Pac-Man)
    pygame.draw.circle(screen, YELLOW, player.center, PLAYER_SIZE // 2)
    
    # Draw score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f'Score: {score}', True, WHITE)
    screen.blit(score_text, (10, 10))

    # Game over text and restart option
    if game_over:
        game_over_text = font.render('You Win!' if not dots else 'Game Over!', True, WHITE)
        text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20))
        screen.blit(game_over_text, text_rect)
        restart_text = font.render('Press SPACE to restart', True, WHITE)
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30))
        screen.blit(restart_text, restart_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
