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
pipe_width = 80
pipe_gap = 200
pipe_speed = 3
pipes = []

# Function to create a new pipe pair
def create_pipe():
    pipe_height = random.randint(100, 400)
    top_pipe = pygame.Rect(800, 0, pipe_width, pipe_height)
    bottom_pipe = pygame.Rect(800, pipe_height + pipe_gap, pipe_width, 600 - pipe_height - pipe_gap)
    return top_pipe, bottom_pipe

def reset_game():
    global bird, bird_movement, pipes, pipe_timer, running, game_over
    bird = pygame.Rect(100, 300, 40, 30)
    bird_movement = 0.0
    pipes = [create_pipe()]
    pipe_timer = 0
    running = True
    game_over = False

# Create initial pipes
pipes.append(create_pipe())
pipe_timer = 0
game_over = False
running = True

font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 40)

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
        for pipe_pair in pipes[:]:  # Use slice copy to safely modify list
            top_pipe, bottom_pipe = pipe_pair
            top_pipe.x -= pipe_speed
            bottom_pipe.x -= pipe_speed

            # Remove pipes that are off screen
            if top_pipe.right < 0:
                pipes.remove(pipe_pair)

        # Check collisions with pipes
        for top_pipe, bottom_pipe in pipes:
            bird_rect = bird.inflate(-10, -10)  # Slightly smaller rect for collision
            if bird_rect.colliderect(top_pipe) or bird_rect.colliderect(bottom_pipe):
                game_over = True

    # Clear screen and draw
    screen.fill((135, 206, 235))  # Sky blue background

    # Draw pipes
    for top_pipe, bottom_pipe in pipes:
        pygame.draw.rect(screen, (0, 128, 0), top_pipe)      # Green top pipe
        pygame.draw.rect(screen, (0, 128, 0), bottom_pipe)   # Green bottom pipe

    # Draw bird
    pygame.draw.rect(screen, (255, 255, 0), bird)  # Yellow bird

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