

import pygame   
pygame.init()
screen = pygame.display.set_mode((800, 600))    
running = True
ball_pos = [400, 300]   
ball_speed = [2, 2]
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]
    if ball_pos[0] <= 0 or ball_pos[0] >= 800:
        ball_speed[0] = -ball_speed[0]
    if ball_pos[1] <= 0 or ball_pos[1] >= 600:
        ball_speed[1] = -ball_speed[1]
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 255, 255), ball_pos, 15)
    pygame.display.flip()
    pygame.time.delay(10)
pygame.quit()

# This code creates a simple ping pong game where a ball bounces around the window.

# how to run:
# 1. Make sure you have Python and Pygame installed.
# 2. Save this code to a file named `ping_pong.py`.
# 3. Run the script using the command `python ping_pong.py`.    


