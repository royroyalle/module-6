import pygame

pygame.init()

screen_width, screen_height = 500, 500

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('Adding image and bg')

background_image = pygame.transform.scale(pygame.image.load('bg.jpg').convert(),(screen_width, screen_height))

penguin_image = pygame.transform.scale(pygame.image.load('Toji.png').convert_alpha(), (500, 500))

penguin_rect = penguin_image.get_rect(center=(screen_width // 2, screen_height // 2 - 30))

text = pygame.font.Font(None, 36,).render('Toji Fushigaro', True, pygame.Color('black'))

text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2 + 110))

def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(background_image, (0, 0))
        screen.blit(penguin_image, penguin_rect)
        screen.blit(text, text_rect)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
if __name__ == '__main__':
    game_loop()
