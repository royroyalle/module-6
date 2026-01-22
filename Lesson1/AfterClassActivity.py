import pygame
pygame.init()

screen_width, screen_height = 500, 500

screen = pygame.display.set_mode((500, 500))

pygame.display.set_caption('My first game screen')

background_image = pygame.transform.scale(pygame.image.load('grey.jpg').convert(),(screen_width, screen_height))

image = pygame.transform.scale(pygame.image.load('Toji.png').convert_alpha(), (300, 300))

image_rect = image.get_rect(center=(screen_width // 2, screen_height // 2 - 30))

def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(background_image, (0, 0))
        screen.blit(image, image_rect)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
if __name__ == '__main__':
    game_loop()
