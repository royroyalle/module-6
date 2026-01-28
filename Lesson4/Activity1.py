import pygame
import random
screen_width, screen_height = 500, 400
movement_speed = 5
font_size = 72
pygame.init()
bg = pygame.image.load("bg.jpg")
bg = pygame.transform.scale(bg, (500, 400))

font = pygame.font.SysFont("Times New Roman", font_size)
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.Color('dodgerblue'))
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()
    def move(self, x_change, y_change):
        self.rect.x = max(min(self.rect.x + x_change, screen_width - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + y_change, screen_height - self.rect.height), 0)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Colision")
all_sprites = pygame.sprite.Group()
sprite1 = Sprite(pygame.Color('black'), 20, 30)
sprite1.rect.x, sprite1.rect.y = random.randint(0, screen_width - sprite1.rect.y), random.randint(0, screen_width - sprite1.rect.y)
all_sprites.add(sprite1)
sprite2 = Sprite(pygame.Color('red'), 20, 30)
sprite2.rect.x, sprite2.rect.y = random.randint(0, screen_width - sprite2.rect.y), random.randint(0, screen_height - sprite2.rect.y)
all_sprites.add(sprite2)
running, won = True, False
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type ==  pygame.KEYDOWN and event.type == pygame.K_x):
            running = False
    if not won:
        keys = pygame.key.get_pressed()
        x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT] * movement_speed)
        y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP] * movement_speed)
        sprite1.move(x_change, y_change)
        if sprite1.rect.colliderect(sprite2.rect):
            all_sprites.remove(sprite2)
            won = True
    screen.blit(bg, (0, 0))
    all_sprites.draw(screen)
    if won:
        win_text = font.render("You win!", True, pygame.Color('black'))
        screen.blit(win_text, ((screen_width - win_text.get_width())//2, (screen_height - win_text.get_height())// 2))
    pygame.display.flip()
pygame.quit()