'''
Basketball
Colton Amoriell
Put the basketball on the sceen

'''
import pygame
# Import sys
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((640,480))
my_image = pygame.image.load("assignments/code_jam/images/basketball.png").convert_alpha()
image_rect = my_image.get_rect(center=(320, 240))



running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill((255, 255, 0))



    screen.blit(my_image, image_rect)
    pygame.display.flip()
    clock.tick(60)
