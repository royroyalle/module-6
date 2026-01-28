import pygame

pygame.init()

screen = pygame.display.set_mode((500, 400))

bg = pygame.image.load("bg.jpg")

bg = pygame.transform.scale(bg, (500, 400))

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False
    screen.blit(bg, (0, 0))
    pygame.display.flip()
pygame.quit()