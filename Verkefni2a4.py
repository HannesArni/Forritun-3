# coding=UTF-8

# Hannes Árni Hannesson 18/10/18
# Þú stýrir litlum kassa og búið er að búa til rauða enemies sem raðast randomly á skjánum

import pygame
import random
# Ég næ ekki þessu library og finnst litirnir hvort eð er ljótir
# from color_library import *

pygame.init()


# Einfaldur klasi, Player
class Player(object):
    def __init__(self, x, y, sx, sy):
        self.rect = pygame.Rect(x, y, sx, sy)

    # fallið move uppfærir hnitin á playernum.
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        # Ef player rekst á einhvern enemy breytist sá enemy í grænann
        for enemy in enemy_list:
            if self.rect.colliderect(enemy.rect):
                enemy.color = (0, 255, 0)


# Mjög einfaldur enemy klasi, maður setur inn staðsetningu óvinsins og lit hans.
class Enemy(object):
    def __init__(self, x, y, color):
        self.rect = pygame.Rect(x, y, 10, 40)
        self.color = color


RED = (255, 0, 0)
ORANGE = (150, 75, 0)
BLACK = (1, 15, 30)
WINDOW_SIZE = (320, 240)

# Notað til að velja á milli wrap around og boundary check
use_wrap_around = True

pygame.display.set_caption("Verkefni 2a4")
screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()

# smíðum Player object og setjum í breytuna player
player = Player(2, 2, 16, 16)
# smíðum mirror sem verður notaður þegar kassinn á að birtast báðum megin skjásins
mirror = Player(0, -16, 16, 16)

# Búum hér til 8 enemies sem mega ekki snerta hvorn annan né playerinn.
enemy_list = []
for x in range(8):
    while True:
        # Búum til enemy sem við erum að vinna með í þessarri keyrslu lykkjunnar
        working_enemy = Enemy(random.randint(0, 310), random.randint(0, 200), RED)
        collision = False
        # Rennum í gegnum alla enemies sem eru í enemy_list og og tékkum hvort það sé snerting á óvinum eða spilara.
        for enemy in enemy_list:
            if enemy.rect.colliderect(working_enemy) or working_enemy.rect.colliderect(player.rect):
                collision = True
        # Ef working_enemy hefur ekki rekist í neitt er honum bætt í listann og brotist er úrúr while True lykkjunni
        if not collision:
            enemy_list.append(working_enemy)
            break

running = True

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False

    # Hreyfum spilarann eftir því hvaða ör notandinn ýtir á.
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.move(-2, 0)
    if key[pygame.K_RIGHT]:
        player.move(2, 0)
    if key[pygame.K_UP]:
        player.move(0, -2)
    if key[pygame.K_DOWN]:
        player.move(0, 2)

    # Gerum wrap around-ið
    if use_wrap_around:
        # Látum mirror-inn endalaust vera á sama stað og playerinn
        mirror.rect.x = player.rect.x
        mirror.rect.y = player.rect.y
        # Tékkum fyrst á vinsti hliðinni
        if player.rect.x < 0:
            # Látum mirror-inn birtast hægra megin, hann fer öfugt mikið inn á skjáinn miðað við playerinn
            mirror.rect.x = 320+player.rect.x
            # Ef playerinn er alveg horfinn færum við hann yfir hinum megin
            if player.rect.x <= -16:
                player.rect.x = 304
        # Hægri hlið
        if player.rect.x > 304:
            mirror.rect.x = -16 + player.rect.x-304
            if player.rect.x >= 320:
                player.rect.x = 0
        # Efri hlið
        if player.rect.y < 0:
            mirror.rect.y = 240+player.rect.y
            if player.rect.y <= -16:
                player.rect.y = 224
        # Neðri hlið
        if player.rect.y > 224:
            mirror.rect.y = -16 + player.rect.y -224
            if player.rect.y >= 240:
                mirror.rect.x = -16
                player.rect.y = 0
    # Notað basic boundary check, ef að notandi hefur fært player-inn eitthvað útaf skjánum færir þetta hann aftur
    else:
        # Vinstri hlið
        if player.rect.x < 0:
            player.move(2, 0)
        # Hægri hlið
        if player.rect.x > 304:
            player.move(-2, 0)
        # Efri hlið
        if player.rect.y < 0:
            player.move(0, 2)
        # Neðri hlið
        if player.rect.y > 224:
            player.move(0, -2)

    # Teiknum allt heila klabbið
    screen.fill(BLACK)
    pygame.draw.rect(screen, ORANGE, player.rect)
    pygame.draw.rect(screen, ORANGE, mirror.rect)
    for x in enemy_list:
        pygame.draw.rect(screen, x.color, x)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
