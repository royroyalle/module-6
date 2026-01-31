
import pygame
import random

pygame.init()

sprite_color_change_event = pygame.USEREVENT + 1
background_color_change_event = pygame.USEREVENT + 2

Blue = pygame.Color('blue')
Light_Blue = pygame.Color('lightblue')
Dark_Blue = pygame.Color('darkblue')
Yellow = pygame.Color('yellow')
Magenta = pygame.Color('magenta')
Orange = pygame.Color('orange')
White = pygame.Color('white')

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-2, 2]), random.choice([-2, 2])]

    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = False

        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True

        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True

        if boundary_hit: 
            pygame.event.post(pygame.event.Event(sprite_color_change_event))
            pygame.event.post(pygame.event.Event(background_color_change_event))

    def change_color(self):
        self.image.fill(random.choice([Yellow, Magenta, Orange, White]))

def change_background_color():
    global bg_color
    bg_color = random.choice([Blue, Light_Blue, Dark_Blue])

all_sprites_list = pygame.sprite.Group()

for _ in range(2):
    sp = Sprite(White, 20, 30)
    sp.rect.x = random.randint(50, 450)
    sp.rect.y = random.randint(50, 350)
    all_sprites_list.add(sp)

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Boundary Sprite")
bg_color = Blue
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == sprite_color_change_event:
            for sprite in all_sprites_list:
                sprite.change_color()
        elif event.type == background_color_change_event:
            change_background_color()

    all_sprites_list.update()
    screen.fill(bg_color)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()