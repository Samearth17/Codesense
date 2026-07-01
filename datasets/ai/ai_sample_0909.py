import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
# Define the class car which represents the car
# It contains the car image, the starting position, the x and y movement
class Car(pygame.sprite.Sprite):
    def __init__(self):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
 
        self.image = pygame.image.load("car.png").convert()
        self.image.set_colorkey(BLACK) 
 
        self.rect = self.image.get_rect()
        self.rect.x = 350
        self.rect.y = 400
        self.change_x = 0
        self.change_y = 0
 
    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
 
# Initializes the game 
pygame.init()
screen_width = 700
screen_height = 500

screen = pygame.display.set_mode([screen_width, screen_height])
 
#Initializes all sprites
car_sprite_list = pygame.sprite.Group()
car = Car()
car_sprite_list.add(car)
 
#This is the main loop of the game
clock = pygame.time.Clock()
done = False
 
while not done:
    #Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    #Update the movement of the car
    car_sprite_list.update()
 
    #Draw everything
    screen.fill(WHITE)
 
    car_sprite_list.draw(screen)
 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()