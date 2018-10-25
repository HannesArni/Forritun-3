# coding=UTF-8

# Hannes Árni Hannesson 25/10/18
# Maze með skjöldum og óvinum, markmiðið er að komast að rauða hliðinu í horninu
# Einungis er hægt að vera með einn skjöld í einu og það þarf að brjóta 7 sprengjur til þess að hliðið opnist
# Maður brýtur sprengjur með því að vera með skjöjld, ef maður fer á sprengjur án þess að vera með skjöld springur maður
# Núna er búið að búa til stærra map.

import pygame
from color_library import *
from texting import text_to_screen

pygame.init()


class Player:
    def __init__(self):
        self.image = pygame.image.load('images2/player16x16.png')
        self.rect = self.image.get_rect()
        self.rect.x = 16
        self.rect.y = 16
        self.shield = False
        self.score = 0
        self.win = False

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

        # Tékkum hvort TOD sé að snerta eitthvað af veggjunum
        for brick in bricks:
            if self.rect.colliderect(brick.rect):
                if dx > 0:
                    self.rect.right = brick.rect.left
                if dx < 0:
                    self.rect.left = brick.rect.right
                if dy > 0:
                    self.rect.bottom = brick.rect.top
                if dy < 0:
                    self.rect.top = brick.rect.bottom

        # Þegar TOD lendir á gate
        if self.rect.colliderect(gate.rect):
            if gate.closed:
                self.rect.x -= dx
                self.rect.y -= dy
        # Tékkum hvort TOD sé kominn út fyrir skjáinn
        if self.rect.x >= WINDOW_SIZE[0]:
            self.win = True

        # Þegar TOD lendir á skjöld verður hann shielded og skjöldurinn hverfu
        # Myndin verður líka tinted
        index = self.rect.collidelist(shields)
        if index >= 0:
            self.shield = True
            self.image.fill((0, 0, 200, 100), special_flags=pygame.BLEND_ADD)
            shields.pop(index)

        # þegar TOD lendir á sprengjum þá hverfa þær af skjánum.
        index = self.rect.collidelist(bombs)
        if index >= 0:
            bombs.pop(index)
            # Ef TOD er shielded er skjöldurinn tekinn í burtu og bætt er við score-ið
            if self.shield:
                self.shield = False
                self.image = pygame.image.load('images2/player16x16.png')
                self.score += 1
            # Ef TOD er ekki með skjöld
            else:
                # Stækkum kassann það mikið að hann kemst ekki inn í völundarhúsið og skýst þá í burtu
                self.rect.inflate_ip(40, 40)
                self.rect.x = -100


class Brick:
    def __init__(self, pos_x, pos_y):
        self.image = pygame.image.load('images2/brick16x16.png')
        self.pos = (pos_x, pos_y)
        self.rect = self.image.get_rect(x=pos_x, y=pos_y)


class Bomb:
    def __init__(self, pos_x, pos_y):
        self.image = pygame.image.load('images2/bomb16x16.png')
        self.pos = (pos_x, pos_y)
        self.rect = self.image.get_rect(x=pos_x, y=pos_y)


class Shield:
    def __init__(self, pos_x, pos_y):
        self.image = pygame.image.load('images2/shield16x16.png')
        self.pos = (pos_x, pos_y)
        self.rect = self.image.get_rect(x=pos_x, y=pos_y)


class Gate:
    def __init__(self, pos_x, pos_y):
        self.image = pygame.image.load('images2/bomb16x16.png')
        self.pos = (pos_x, pos_y)
        self.rect = self.image.get_rect(x=pos_x, y=pos_y)
        self.closed = True


# Aðal leikurinn, hérna er hægt að spila hann
def main_game():
    # Move the player if an arrow key is pressed
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        tod.move(-2, 0)
    if key[pygame.K_RIGHT]:
        tod.move(2, 0)
    if key[pygame.K_UP]:
        tod.move(0, -2)
    if key[pygame.K_DOWN]:
        tod.move(0, 2)

    # Tékkað hvort TOD sé með nóg stig til þess að opna hliðið
    if tod.score > 6:
        gate.closed = False

    screen.fill(DARKOLIVEGREEN)
    # allir múrsteinarnir í listanum eru teiknaðir
    for brick in bricks:
        screen.blit(brick.image, brick.pos)

    # allar sprengjurnar teiknaðar
    for bomb in bombs:
        screen.blit(bomb.image, bomb.pos)

    # allir skildir teiknaðir
    for shield in shields:
        screen.blit(shield.image, shield.pos)

    # hliðið teiknað
    if gate.closed:
        pygame.draw.rect(screen, DARKRED, gate)
    else:
        pygame.draw.rect(screen, DARKOLIVEGREEN, gate)

    # sjálfur TOD teiknaður
    screen.blit(tod.image, tod.rect)


# Lokaskjár, búið er að vinna
def end_screen():
    screen.fill(DARKOLIVEGREEN)
    text = "Winner!"
    text_to_screen(screen, text, (WINDOW_SIZE[0]/2)-len(text)*10, WINDOW_SIZE[1]/2 - 40)


WINDOW_SIZE = (640, 352)
pygame.display.set_caption('K2 Leikjaforritun')
screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()

tod = Player()
bricks = list()
bombs = list()
shields = list()
gate = None

# hér er kortið sem notað er í leiknum, W = veggur, E = útgönguleið, B = sprengja, S = skjöldur
map = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W    B        SWS     B   SW   WS     SW",
    "W       WWWWWWWW   WWWWWWWWW W WS     SW",
    "W   WWWWW   B SWW  W    B    W WWWWWWBBW",
    "W   W        WWSW  W    WWWWWW W       W",
    "W WWW  WWWW    BWWBW    WB     WWBWWWWWW",
    "W   W     W             W  WWWWWW      W",
    "W   W   B W   WWWWWWWWWWW  W    W      W",
    "W   WWW WWW   WSW  B  S    W    W      W",
    "W     W D W   W W  WWWWWWWWW WWWWWWWWWWW",
    "WWW   W   WWWWWBW  WB      W           W",
    "WSW      WW        W               B B W",
    "W W   WWWW   WWWWWWWWWWWWWWWWWWWWWWW WWW",
    "WBWWW WSSB   W    B          W     B BBE",
    "W            W    W          W         W",
    "W          B W    W          W         W",
    "W            W    W          W         W",
    "W    S       WWWW WWWWWW     WWWWWWWWBBW",
    "WB                W    W               W",
    "WWWWWWWWWWWW WWWWWW SS WWWWWWWWWWWWWWWBW",
    "WS   B        B        W  S            W",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
]

# Hér þarf að "parsa völundarhúsið". W = veggur, E = útgönguleið, B = sprengja, S = skjöldur
x = y = 0

# Förum í gegnum mappið og setjum allt á þann stað sem það þarf að vera
for row in map:
    for col in row:
        if col == "W":
            bricks.append(Brick(x, y))
        if col == "B":
            bombs.append(Bomb(x, y))
        if col == "S":
            shields.append(Shield(x, y))
        if col == "E":
            gate = Gate(x, y)
        x += 16
    y += 16
    x = 0

running = True

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False

    if not tod.win:
        main_game()
    else:
        end_screen()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
