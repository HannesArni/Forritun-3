# coding=UTF-8

# Hannes Árni Hannesson 25/10/18
# Hér stýrir maður litlum kassa og á að reyna að komast framhjá öllum kössunum sem eru að hreyfast í kring.
# Ýtt er á ESC til þess að byrja aftur

import pygame
import random


class Box(pygame.sprite.Sprite):
    def __init__(self, window, color, width, height):
        super(Box, self).__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.screen = window
        self.rect = self.image.get_rect()
        self.speed_x = random.randint(-10, 10)
        self.speed_y = random.randint(-5, 5)

    def update(self):
        self.rect.left += self.speed_x
        self.rect.top += self.speed_y
        if self.rect.right > self.screen.get_width() or self.rect.left < 0:
            self.speed_x = -self.speed_x
        if self.rect.bottom > self.screen.get_height() or self.rect.top < 0:
            self.speed_y = -self.speed_y


# Player klasi
class Player(pygame.sprite.Sprite):
    def __init__(self, window, width, height, pos_y, pos_x):
        super(Player, self).__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((0, 0, 0))
        self.screen = window
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos_y, pos_x

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy


pygame.init()
clock = pygame.time.Clock()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
BLOCK_WIDTH = 30
BLOCK_HEIGHT = 30

WHITE = (255, 255, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
pygame.display.set_caption("So Many Blocks")
blocksGroup = pygame.sprite.Group()

# Allir enemies búnir til
for x in range(8):
    r = random.randint(50, 255)
    g = random.randint(50, 255)
    b = random.randint(50, 255)
    myBox = Box(screen, (r, g, b), BLOCK_WIDTH, BLOCK_HEIGHT)

    myBox.rect.x = random.randrange(SCREEN_WIDTH - BLOCK_WIDTH)
    myBox.rect.y = random.randrange(SCREEN_HEIGHT - BLOCK_HEIGHT)
    blocksGroup.add(myBox)

# player búinn til
player = Player(screen, BLOCK_WIDTH, BLOCK_HEIGHT, 300, 500)
player_speed = 4
running = True
pause = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            player.rect.y = 500
            player.rect.x = 300
            pause = False

    if not pause:
        screen.fill(WHITE)

        # Tökum key input og notum það til þess að hreyfa playerinn.
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            player.move(-player_speed, 0)
        if key[pygame.K_RIGHT]:
            player.move(player_speed, 0)
        if key[pygame.K_UP]:
            player.move(0, -player_speed)
        if key[pygame.K_DOWN]:
            player.move(0, player_speed)

        # Tékkum hvort playerinn sé kominn fyrir ofan skjáinn, ef svo er er pásað
        if player.rect.y <= 0 and  0 <= player.rect.x <= SCREEN_WIDTH:
            pause = True
        # Tékkum hvort playerinn sé að collida við einhvern og ef svo er er hann teiknaður annars er hann færður burt
        if pygame.sprite.spritecollideany(player, blocksGroup) is None:
            screen.blit(player.image, (player.rect.x, player.rect.y))
        else:
            player.rect.x = 50000
            pause = True

        blocksGroup.update()
        blocksGroup.draw(screen)
        pygame.display.update()
        clock.tick(40)

pygame.quit()
