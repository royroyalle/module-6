import pygame

pygame.init()

screen_width, screen_height = 500, 500
screen = pygame.display.set_mode((screen_width, screen_height))
shape_width, shape_height = 100, 100
x, y = 200, 200
RED = (100, 0, 0)
pygame.display.set_caption('First Game Screen Of Rohith')

pygame.draw.rect(screen, RED,( x, y, shape_width, shape_height), 0 ) 

text = pygame.font.Font(None, 36).render('First Game Screen', True, pygame.Color('red'))
text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2 + 110))

def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(text, text_rect)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
if __name__ == '__main__':
    game_loop()