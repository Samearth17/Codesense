"""
A game loop for a game of Pong using Python
"""
import pygame
import time

# Define constants
BLACK = (0, 0, 0)
WIDTH = 600
HEIGHT = 400
RADIUS = 20
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 75 

# Initialize game
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong") 
center_point = WIDTH/2, HEIGHT/2
clock = pygame.time.Clock()

# Game variables
paddleA_y = HEIGHT / 2
paddleB_y = HEIGHT / 2
ball_x = WIDTH / 2
ball_y = HEIGHT / 2
ball_change_x = 2
ball_change_y = 2

# Begin game loop
while True:
    # Reset screen
    screen.fill(BLACK)
    
    # Drawing objects
    ball = pygame.draw.circle(screen, (255,255,255), (int(ball_x), int(ball_y)), RADIUS)
    paddleA = pygame.draw.rect(screen, (255,255,255), (0, paddleA_y, PADDLE_WIDTH, PADDLE_HEIGHT)) 
    paddleB = pygame.draw.rect(screen, (255,255,255), (WIDTH - PADDLE_WIDTH, paddleB_y, PADDLE_WIDTH, PADDLE_HEIGHT))
	
    # Event loop 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()

    # Movement of paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA_y -= 3
    elif keys[pygame.K_s]:
        paddleA_y += 3
    elif keys[pygame.K_UP]:
        paddleB_y -= 3
    elif keys[pygame.K_DOWN]:
        paddleB_y += 3

    # Limit the position of the paddles
    if paddleA_y < 0:
       paddleA_y = 0
    elif paddleA_y > HEIGHT - PADDLE_HEIGHT:
       paddleA_y = HEIGHT - PADDLE_HEIGHT
    if paddleB_y < 0:
       paddleB_y = 0
    elif paddleB_y > HEIGHT - PADDLE_HEIGHT:
       paddleB_y = HEIGHT - PADDLE_HEIGHT

    # Ball bouncing to the left
    if (ball.left <= paddleA.right + 10) and ball.colliderect(paddleA):
        ball_change_x = -ball_change_x

    # Ball bouncing to the right
    if (ball.right >= paddleB.left - 10) and ball.colliderect(paddleB):
        ball_change_x = -ball_change_x

    # Ball bouncing up
    if (ball.top <= 0) or (ball.bottom >= HEIGHT):
        ball_change_y = -ball_change_y
    
    # Ball movement
    ball_x += ball_change_x
    ball_y += ball_change_y
	
    #Update display
    pygame.display.flip()
    clock.tick(30)