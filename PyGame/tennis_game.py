# create tennis game
import pygame   
import time
import random  # Add this for random miss chance
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
OPPONENT_BAT_COLOR = ORANGE

# Initialize player bat position
bat_x = 50
bat_y = 250
bat_width = 20
bat_height = 100
bat_speed = 5

# Initialize opponent bat position
opponent_bat_x = SCREEN_WIDTH - 50 - bat_width
opponent_bat_y = 250
opponent_bat_speed = 5

# Initialize ball position and movement
ball_x = 400
ball_y = 300
ball_radius = 15
ball_speed_x = 3
ball_speed_y = 2
ball_speed_increment = 0.5  # Speed increase per round

# Initialize scores
player_score = 0
opponent_score = 0
WINNING_SCORE = 5
game_over = False

# Initialize font for score display
font = pygame.font.Font(None, 74)
countdown_font = pygame.font.Font(None, 100)

# Ball reset state
resetting = False
reset_start_time = 0
reset_countdown = 3  # seconds

rounds_played = 0  # Track how many points have been scored

miss_chance = 0.45  # Probability (0-1) that the computer will "miss" the ball per frame

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
                ball_speed_x = 3
                ball_speed_y = 2
                rounds_played = 0
                resetting = False

    if not game_over:
        # Ball reset countdown logic
        if resetting:
            elapsed = time.time() - reset_start_time
            countdown = max(0, reset_countdown - int(elapsed))
            if elapsed >= reset_countdown:
                resetting = False
        else:
            # Get pressed keys for smooth movement
            keys = pygame.key.get_pressed()
            
            # Move player bat up and down with arrow keys or W/S keys
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                bat_y -= bat_speed
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                bat_y += bat_speed
            
            # Keep player bat within screen boundaries
            if bat_y < 0:
                bat_y = 0
            if bat_y > SCREEN_HEIGHT - bat_height:
                bat_y = SCREEN_HEIGHT - bat_height

            # Move opponent bat (simple AI: follow the ball, but with a chance to miss)
            if not resetting and abs(ball_speed_x) > 0 and ball_speed_x > 0:
                # Only try to follow if ball is moving toward the opponent
                if random.random() > miss_chance:
                    if ball_y < opponent_bat_y + bat_height // 2:
                        opponent_bat_y -= opponent_bat_speed
                    elif ball_y > opponent_bat_y + bat_height // 2:
                        opponent_bat_y += opponent_bat_speed
                # else: do nothing this frame (simulate a miss)
            # Keep opponent bat within screen boundaries
            if opponent_bat_y < 0:
                opponent_bat_y = 0
            if opponent_bat_y > SCREEN_HEIGHT - bat_height:
                opponent_bat_y = SCREEN_HEIGHT - bat_height

            # Move the ball
            ball_x += ball_speed_x
            ball_y += ball_speed_y
            
            # Ball collision with top and bottom walls
            if ball_y <= ball_radius or ball_y >= SCREEN_HEIGHT - ball_radius:
                ball_speed_y = -ball_speed_y
            
            # Ball collision with right wall (opponent scores)
            if ball_x >= SCREEN_WIDTH - ball_radius:
                opponent_score += 1
                # Reset ball position and start countdown
                ball_x = SCREEN_WIDTH // 2
                ball_y = SCREEN_HEIGHT // 2
                # Increase speed for next round
                rounds_played += 1
                speed_sign_x = -1 if ball_speed_x < 0 else 1
                speed_sign_y = -1 if ball_speed_y < 0 else 1
                ball_speed_x = speed_sign_x * (3 + rounds_played * ball_speed_increment)
                ball_speed_y = speed_sign_y * (2 + rounds_played * ball_speed_increment)
                ball_speed_x = -abs(ball_speed_x)
                resetting = True
                reset_start_time = time.time()
            
            # Ball collision with left wall (player scores)
            if ball_x <= ball_radius:
                player_score += 1
                # Reset ball position and start countdown
                ball_x = SCREEN_WIDTH // 2
                ball_y = SCREEN_HEIGHT // 2
                # Increase speed for next round
                rounds_played += 1
                speed_sign_x = 1 if ball_speed_x > 0 else -1
                speed_sign_y = 1 if ball_speed_y > 0 else -1
                ball_speed_x = speed_sign_x * (3 + rounds_played * ball_speed_increment)
                ball_speed_y = speed_sign_y * (2 + rounds_played * ball_speed_increment)
                ball_speed_x = abs(ball_speed_x)
                resetting = True
                reset_start_time = time.time()
            
            # Check for game over
            if player_score >= WINNING_SCORE or opponent_score >= WINNING_SCORE:
                game_over = True
            
            # Ball collision with player bat
            if (ball_x - ball_radius <= bat_x + bat_width and 
                ball_x + ball_radius >= bat_x and 
                ball_y + ball_radius >= bat_y and 
                ball_y - ball_radius <= bat_y + bat_height and
                ball_speed_x < 0):
                ball_speed_x = -ball_speed_x

            # Ball collision with opponent bat
            if (ball_x + ball_radius >= opponent_bat_x and
                ball_x - ball_radius <= opponent_bat_x + bat_width and
                ball_y + ball_radius >= opponent_bat_y and
                ball_y - ball_radius <= opponent_bat_y + bat_height and
                ball_speed_x > 0):
                ball_speed_x = -ball_speed_x

    # Drawing
    screen.fill(BACKGROUND_COLOR)
    # Draw player bat
    pygame.draw.rect(screen, BAT_COLOR, (bat_x, bat_y, bat_width, bat_height))
    # Draw opponent bat
    pygame.draw.rect(screen, OPPONENT_BAT_COLOR, (opponent_bat_x, opponent_bat_y, bat_width, bat_height))
    # Draw ball
    pygame.draw.circle(screen, BALL_COLOR, (int(ball_x), int(ball_y)), ball_radius)
    
    # Draw scores
    player_text = font.render(str(player_score), True, WHITE)
    opponent_text = font.render(str(opponent_score), True, WHITE)
    screen.blit(player_text, (SCREEN_WIDTH * 3/4, 20))
    screen.blit(opponent_text, (SCREEN_WIDTH * 1/4, 20))
    
    # Draw countdown if resetting
    if not game_over and resetting:
        elapsed = time.time() - reset_start_time
        countdown = max(1, reset_countdown - int(elapsed))
        countdown_text = countdown_font.render(str(countdown), True, BLACK)
        screen.blit(countdown_text, (SCREEN_WIDTH//2 - countdown_text.get_width()//2, SCREEN_HEIGHT//2 - countdown_text.get_height()//2))

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

# This code initialises a Pygame window for a tennis game with user-controlled bat movement.
# Use arrow keys or W/S keys to move the bat up and down.
# The bat is constrained to stay within the screen boundaries. 

# how to run:
# 1. Make sure you have Python and Pygame installed.
# 2. Save this script as `tennis_game.py`.
# 3. Run the script using the command: python tennis_game.py
