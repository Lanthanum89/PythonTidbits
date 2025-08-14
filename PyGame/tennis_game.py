# create tennis game
import pygame   
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Define colors (R, G, B values from 0-255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)

# Color choices - change these to customize your game!
BACKGROUND_COLOR = PURPLE
BAT_COLOR = CYAN
BALL_COLOR = YELLOW

# Initialize bat position
bat_x = 50
bat_y = 250
bat_width = 20
bat_height = 100
bat_speed = 5

# Initialize ball position and movement
ball_x = 400
ball_y = 300
ball_radius = 15
ball_speed_x = 3
ball_speed_y = 2

# Initialize scores
player_score = 0
opponent_score = 0
WINNING_SCORE = 5
game_over = False

# Initialize font for score display
font = pygame.font.Font(None, 74)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Add key press to restart game when it's over
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_SPACE:
                # Reset the game
                player_score = 0
                opponent_score = 0
                game_over = False
                ball_x = 400
                ball_y = 300
    
    if not game_over:
        # Get pressed keys for smooth movement
        keys = pygame.key.get_pressed()
        
        # Move bat up and down with arrow keys or W/S keys
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            bat_y -= bat_speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            bat_y += bat_speed
        
        # Keep bat within screen boundaries
        if bat_y < 0:
            bat_y = 0
        if bat_y > SCREEN_HEIGHT - bat_height:
            bat_y = SCREEN_HEIGHT - bat_height
        
        # Move the ball
        ball_x += ball_speed_x
        ball_y += ball_speed_y
        
        # Ball collision with top and bottom walls
        if ball_y <= ball_radius or ball_y >= SCREEN_HEIGHT - ball_radius:
            ball_speed_y = -ball_speed_y
        
        # Ball collision with right wall (opponent scores)
        if ball_x >= SCREEN_WIDTH - ball_radius:
            opponent_score += 1
            # Reset ball position
            ball_x = SCREEN_WIDTH // 2
            ball_y = SCREEN_HEIGHT // 2
            ball_speed_x = -ball_speed_x
        
        # Ball collision with left wall (player loses point)
        if ball_x <= ball_radius:
            player_score += 1
            # Reset ball position
            ball_x = SCREEN_WIDTH // 2
            ball_y = SCREEN_HEIGHT // 2
            ball_speed_x = -ball_speed_x
        
        # Check for game over
        if player_score >= WINNING_SCORE or opponent_score >= WINNING_SCORE:
            game_over = True
        
        # Ball collision with bat
        if (ball_x - ball_radius <= bat_x + bat_width and 
            ball_x + ball_radius >= bat_x and 
            ball_y + ball_radius >= bat_y and 
            ball_y - ball_radius <= bat_y + bat_height):
            ball_speed_x = -ball_speed_x
    
    # Drawing
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, BAT_COLOR, (bat_x, bat_y, bat_width, bat_height))  # Bat
    pygame.draw.circle(screen, BALL_COLOR, (int(ball_x), int(ball_y)), ball_radius)  # Ball
    
    # Draw scores
    player_text = font.render(str(player_score), True, WHITE)
    opponent_text = font.render(str(opponent_score), True, WHITE)
    screen.blit(player_text, (SCREEN_WIDTH * 3/4, 20))
    screen.blit(opponent_text, (SCREEN_WIDTH * 1/4, 20))
    
    # Draw game over message
    if game_over:
        winner = "Player 2" if player_score > opponent_score else "Player 1"
        game_over_text = font.render(f"{winner} Wins!", True, WHITE)
        restart_text = font.render("Press SPACE to restart", True, WHITE)
        screen.blit(game_over_text, (SCREEN_WIDTH//2 - 100, SCREEN_HEIGHT//2 - 50))
        screen.blit(restart_text, (SCREEN_WIDTH//2 - 200, SCREEN_HEIGHT//2 + 50))

    pygame.display.flip()
    pygame.time.delay(10)

pygame.quit()

# This code initializes a Pygame window for a tennis game with user-controlled bat movement.
# Use arrow keys or W/S keys to move the bat up and down.
# The bat is constrained to stay within the screen boundaries. 

# how to run:
# 1. Make sure you have Python and Pygame installed.
# 2. Save this script as `tennis_game.py`.
# 3. Run the script using the command: python tennis_game.py
