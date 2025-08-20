# create flappy bird game
import pygame
import random
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

bird = pygame.Rect(100, 300, 40, 30)
gravity = 0.5
bird_movement = 0.0

# Obstacle (pipe) settings
pipe_gap = 200
pipe_speed = 3
pipes = []

# Score and high score
score = 0
highscore_file = "flappy_highscore.txt"
try:
    with open(highscore_file, "r") as f:
        highscore = int(f.read())
except:
    highscore = 0

# Add pipe color and width varieties
PIPE_COLORS = [(0, 128, 0), (34, 139, 34), (0, 200, 0), (60, 179, 113), (107, 142, 35)]
PIPE_WIDTHS = [60, 80, 100]

# Cloud settings
CLOUD_COLOR = (255, 255, 255)
CLOUDS = [
    {"x": 100, "y": 80, "speed": 0.5, "size": 40},
    {"x": 300, "y": 50, "speed": 0.3, "size": 60},
    {"x": 600, "y": 120, "speed": 0.4, "size": 50},
    {"x": 500, "y": 200, "speed": 0.2, "size": 35},
]

# Function to create a new pipe pair with random color and width
def create_pipe():
    pipe_height = random.randint(100, 400)
    pipe_width = random.choice(PIPE_WIDTHS)
    pipe_color = random.choice(PIPE_COLORS)
    top_pipe = pygame.Rect(800, 0, pipe_width, pipe_height)
    bottom_pipe = pygame.Rect(800, pipe_height + pipe_gap, pipe_width, 600 - pipe_height - pipe_gap)
    return (top_pipe, bottom_pipe, pipe_color)

def save_highscore(new_highscore):
    with open(highscore_file, "w") as f:
        f.write(str(new_highscore))

def reset_game():
    global bird, bird_movement, pipes, pipe_timer, running, game_over, score
    bird = pygame.Rect(100, 300, 40, 30)
    bird_movement = 0.0
    pipes = [create_pipe()]
    pipe_timer = 0
    running = True
    game_over = False
    score = 0

# Create initial pipes
pipes.append(create_pipe())
pipe_timer = 0
game_over = False
running = True

font = pygame.font.SysFont("Comic Sans MS", 74)
small_font = pygame.font.SysFont("Comic Sans MS", 40)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if not game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_movement = -10.0  # Jump when space is pressed
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    reset_game()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

    if not game_over:
        # Apply gravity and movement
        bird_movement += gravity
        bird.y += int(bird_movement)  # Convert to int for Rect

        # Ground collision
        if bird.bottom >= SCREEN_HEIGHT:
            bird.bottom = SCREEN_HEIGHT
            bird_movement = 0.0
            game_over = True

        # Keep bird on screen (top boundary)
        if bird.top <= 0:
            bird.top = 0
            bird_movement = 0.0

        # Move pipes and add new ones
        pipe_timer += 1
        if pipe_timer > 90:  # Add new pipe every 1.5 seconds (90 frames at 60 FPS)
            pipes.append(create_pipe())
            pipe_timer = 0

        # Move and remove pipes
        for pipe_tuple in pipes[:]:  # Use slice copy to safely modify list
            top_pipe, bottom_pipe, pipe_color = pipe_tuple
            top_pipe.x -= pipe_speed
            bottom_pipe.x -= pipe_speed

            # Remove pipes that are off screen
            if top_pipe.right < 0:
                pipes.remove(pipe_tuple)
                score += 1  # Score increases when a pipe leaves the screen

        # Check collisions with pipes
        for top_pipe, bottom_pipe, pipe_color in pipes:
            bird_rect = bird.inflate(-10, -10)  # Slightly smaller rect for collision
            if bird_rect.colliderect(top_pipe) or bird_rect.colliderect(bottom_pipe):
                game_over = True

    else:
        # Save highscore if beaten
        if score > highscore:
            highscore = score
            save_highscore(highscore)

    # Clear screen and draw
    screen.fill((135, 206, 235))  # Sky blue background

    # Move and draw clouds
    for cloud in CLOUDS:
        cloud["x"] += cloud["speed"]
        if cloud["x"] > SCREEN_WIDTH + 60:
            cloud["x"] = -60  # Wrap around
        # Draw cloud as several overlapping circles for a fluffy look
        base_x, base_y, size = int(cloud["x"]), int(cloud["y"]), cloud["size"]
        pygame.draw.circle(screen, CLOUD_COLOR, (base_x, base_y), size)
        pygame.draw.circle(screen, CLOUD_COLOR, (base_x + size//2, base_y + size//3), size//1.5)
        pygame.draw.circle(screen, CLOUD_COLOR, (base_x - size//2, base_y + size//3), size//2)

    # Draw pipes with their individual colors
    for top_pipe, bottom_pipe, pipe_color in pipes:
        pygame.draw.rect(screen, pipe_color, top_pipe)
        pygame.draw.rect(screen, pipe_color, bottom_pipe)

    # Draw bird shadow (ellipse under bird)
    shadow_color = (120, 120, 0, 100)  # semi-transparent dark yellow
    shadow_surface = pygame.Surface((bird.width, bird.height // 2), pygame.SRCALPHA)
    pygame.draw.ellipse(shadow_surface, shadow_color, (0, 0, bird.width, bird.height // 2))
    screen.blit(shadow_surface, (bird.x, bird.y + bird.height // 1.5))

    # Draw bird
    pygame.draw.rect(screen, (255, 255, 0), bird)  # Yellow bird

    # Draw score and highscore
    score_text = small_font.render(f"Score: {score}", True, (0, 0, 0))
    highscore_text = small_font.render(f"Highscore: {highscore}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    screen.blit(highscore_text, (10, 50))

    if game_over:
        # Draw finishing screen
        text = font.render("Game Over!", True, (255, 0, 0))
        retry = small_font.render("Press SPACE to try again or ESC to quit", True, (0, 0, 0))
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - 80))
        screen.blit(retry, (SCREEN_WIDTH // 2 - retry.get_width() // 2, SCREEN_HEIGHT // 2 + 10))

    # Update display
    pygame.display.flip()
    clock.tick(60)  # Limit to 60 FPS

pygame.quit()