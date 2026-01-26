import pygame
def main():
    pygame.init()
    screen_width, screen_height = 500, 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('color changing sprite')
    x, y = 150, 200
    x1, y1 = 350, 200
    spirte_width, sprite_height = 60, 60
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]: x-= 3
        if pressed[pygame.K_RIGHT]: x+= 3
        if pressed[pygame.K_UP]: y-= 3
        if pressed[pygame.K_DOWN]: y+= 3
        color = (200, 0, 0)
        color2 = (0, 200, 0)
        x = min(max(0, x), screen_width - spirte_width)
        y = min(max(0, y), screen_height - sprite_height)
        screen.fill((0, 0 ,0))
        pygame.draw.rect(screen, color, (x, y, spirte_width, sprite_height))
        pygame.draw.rect(screen, color2, (x1, y1, spirte_width, sprite_height))
        pygame.display.flip()
    pygame.quit()
if __name__ == '__main__':
    main()