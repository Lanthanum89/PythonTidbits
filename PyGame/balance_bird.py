# create flappy bird game
import pygame
import random
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

bird = pygame.Rect(100, 300, 40, 30)
gravity = 0.5
bird_movement = 0.0
running = True

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

# Create initial pipes
pipes.append(create_pipe())
pipe_timer = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = -10.0  # Jump when space is pressed
            if event.key == pygame.K_ESCAPE:
                running = False  # Exit the game loop

    # Apply gravity and movement
    bird_movement += gravity
    bird.y += int(bird_movement)  # Convert to int for Rect

    # Ground collision
    if bird.bottom >= 600:
        bird.bottom = 600
        bird_movement = 0.0

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
            running = False  # Game over on collision

    # Clear screen and draw
    screen.fill((135, 206, 235))  # Sky blue background
    
    # Draw pipes
    for top_pipe, bottom_pipe in pipes:
        pygame.draw.rect(screen, (0, 128, 0), top_pipe)      # Green top pipe
        pygame.draw.rect(screen, (0, 128, 0), bottom_pipe)   # Green bottom pipe
    
    # Draw bird
    pygame.draw.rect(screen, (255, 255, 0), bird)  # Yellow bird
    
    # Update display
    pygame.display.flip()
    clock.tick(60)  # Limit to 60 FPS

pygame.quit()  