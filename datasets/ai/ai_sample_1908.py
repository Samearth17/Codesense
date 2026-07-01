import pygame

# Game constants 
WIDTH = 800
HEIGHT = 600
FPS = 30

# Initialize pygame
pygame.init()

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Game loop
running = True
while running:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Logic 

    # Rendering
    screen.fill(0, 0, 0)
    pygame.display.flip()

# Terminates the game
pygame.quit()