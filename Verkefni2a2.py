# coding=UTF-8

# Hannes Árni Hannesson 14/10/18
# Þú stýrir litlum kassa sem getur annaðhvort verið með boundary check eða wrap around, er með fancy mirror stuff

import pygame
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


ORANGE = (150, 75, 0)
BLACK = (1, 15, 30)
WINDOW_SIZE = (320, 240)

# Notað til að velja á milli wrap around og boundary check
use_wrap_around = True

pygame.display.set_caption("Verkefni 2a2")
screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()

# smíðum Player object og setjum í breytuna player
player = Player(40, 40, 16, 16)
# smíðum mirror sem verður notaður þegar kassinn á að birtast báðum megin skjásins
mirror = Player(0, -16, 16, 16)

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
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
