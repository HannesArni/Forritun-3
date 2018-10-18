# coding=UTF-8

# Hannes Árni Hannesson 18/10/18
# Þú stýrir litlum kassa og búið er að búa til rauða enemies sem raðast randomly á skjánum
# Það eru gefin stig og eitthvað gaman

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
        # Ef hann fer til vinstri
        if dx > 0:
            working_color = WHITE
        # Ef hann fer til hægri
        elif dx < 0:
            working_color = GREEN
        else:
            working_color = RED
        # Ef player rekst á einhvern enemy breytist sá enemy í grænann
        for enemy in enemy_list:
            if self.rect.colliderect(enemy.rect):
                enemy.color = working_color


# Mjög einfaldur enemy klasi, maður setur inn staðsetningu óvinsins og lit hans.
class Enemy(object):
    def __init__(self, x, y, color):
        self.rect = pygame.Rect(x, y, 10, 40)
        self.color = color


# Litir
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
ORANGE = (150, 75, 0)
BLACK = (1, 15, 30)

WINDOW_SIZE = (320, 240)
FRAME_RATE = 60
frame_count = 0
time_sec = 0
PLAY_TIME = 10
arial_font = pygame.font.SysFont('arialblack', 150)
smaller_arial = pygame.font.SysFont('arialblack', 75)
very_small_arial = pygame.font.SysFont('arialblack', 15)
high_score = 0

# Notað til að velja á milli wrap around og boundary check
use_wrap_around = True

pygame.display.set_caption("Verkefni 2a5")
screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()

running = starting = playing = initialize = True

while running:
    # Keychecker
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN:
            starting = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_BACKSPACE:
            initialize = True
    screen.fill(BLACK)
    # Búum til allt leikborðið
    if initialize:
        # smíðum Player object og setjum í breytuna player
        player = Player(2, 2, 16, 16)
        # smíðum mirror sem verður notaður þegar kassinn á að birtast báðum megin skjásins
        mirror = Player(0, -16, 16, 16)

        # Búum til 8 enemies sem mega ekki snerta hvorn annan né playerinn.
        enemy_list = []
        for x in range(8):
            while True:
                # Búum til enemy sem við erum að vinna með í þessarri keyrslu lykkjunnar
                working_enemy = Enemy(random.randint(0, 310), random.randint(0, 200), RED)
                collision = False
                # Rennum í gegnum alla enemies sem eru í enemy_list og tékkum hvort það sé snerting á óvinum eða spilara
                for enemy in enemy_list:
                    if enemy.rect.colliderect(working_enemy) or working_enemy.rect.colliderect(player.rect):
                        collision = True
                # Ef working_enemy hefur ekki rekist í neitt
                # er honum bætt í listann og brotist er úrúr while True lykkjunni
                if not collision:
                    enemy_list.append(working_enemy)
                    break

        # Núllstillum það sem þarf að núllstilla fyrir playing
        initialize = False
        playing = True
        frame_count = 0
    # Byrjunarskjár
    elif starting:
        screen.blit(very_small_arial.render(
            'Markmiðið:',
            True,
            RED), (120, 40))
        screen.blit(very_small_arial.render(
            'Fjöldi grænna og hvítra sé sá sami',
            True,
            WHITE), (15, 70))
        screen.blit(very_small_arial.render(
            'á sem stystum tíma',
            True,
            WHITE), (75, 95))
        screen.blit(very_small_arial.render(
            'Backspace = Byrja aftur',
            True,
            GREEN), (60, 140))
        screen.blit(very_small_arial.render(
            'Enter = Halda áfram',
            True,
            GREEN), (70, 170))
    # Verið er að spila
    elif playing:
        # Hreyfum spilarann
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

        # Teiknum timer á miðjann skjáinn
        time_left = PLAY_TIME - time_sec
        # Tékkum hvort tíminn sé búinn, ef svo er hættum við að spila
        if time_left <= 0:
            time_left = 0
            playing = False
        # Búum til time object
        time = arial_font.render(
            str(time_left),
            True,
            (6+time_sec, 21+time_sec, 36+time_sec)
        )
        reds = 0
        # Tékkum hvort búið sé að lita alla kubbana
        for enemy in enemy_list:
            if enemy.color == RED:
                reds += 1
        if reds == 0:
            playing = False

        # Teiknum allt heila klabbið
        screen.blit(
            time,
            (150 - len(str(time_left)) * 50, 15)
        )
        pygame.draw.rect(screen, ORANGE, player.rect)
        pygame.draw.rect(screen, ORANGE, mirror.rect)
        for enemy in enemy_list:
            pygame.draw.rect(screen, enemy.color, enemy)

        # Tökum niður tímann
        frame_count += 1
        time_sec = (frame_count // FRAME_RATE)
    # Leikur kláraður
    else:
        greens = whites = 0
        for enemy in enemy_list:
            if enemy.color == GREEN:
                greens += 1
            elif enemy.color == WHITE:
                whites += 1
        score = 8 + time_left - abs(greens - whites)
        if score > high_score:
            high_score = score
        # Teiknum fjölda grænna
        screen.blit(smaller_arial.render(
            str(greens), True, GREEN),
            (75, 10))
        # Teiknum fjölda hvítra
        screen.blit(smaller_arial.render(
            str(whites), True, WHITE),
            (175, 10))
        # Teiknum stig
        screen.blit(very_small_arial.render(
            'Stig:                  High score:', True, RED),
            (50, 115))
        screen.blit(smaller_arial.render(
            str(score), True, RED),
            (65 - len(str(score)) * 25, 125))
        screen.blit(smaller_arial.render(
            str(high_score), True, RED),
            (230 - len(str(high_score)) * 25, 125))

    # Setjum frame rate
    clock.tick(FRAME_RATE)
    pygame.display.flip()
pygame.quit()
