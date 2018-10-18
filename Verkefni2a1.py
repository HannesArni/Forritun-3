# Hannes Árni Hannesson 14/10/18
# Lætur tvo kassa skjótast um skjáinn, ef þeir snerta hliðarnar eða hvorn annan snúa þeir við

import pygame
import random

pygame.init()

BACKGROUND_COLOR = (1, 22, 27)
WINDOW_SIZE = (960, 540)
RED = (130, 9, 51)
WHITE = (239, 233, 231)

window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Verkefni 2a1")
window.fill(BACKGROUND_COLOR)

# Declare-um alla variables
x1_pos = 1
y1_pos = 2
x2_pos = 860
y2_pos = random.randint(0, 440)
x1_vel = 1
y1_vel = 1
x2_vel = -1
y2_vel = 1
running = True

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False

    window.fill(BACKGROUND_COLOR)

    # Búum til báða kassana
    sq1 = pygame.draw.rect(window, RED, pygame.Rect(x1_pos, y1_pos, 100, 100))
    sq2 = pygame.draw.rect(window, WHITE, pygame.Rect(x2_pos, y2_pos, 100, 100))

    # Hreyfum báða kassana miðað við vel
    x1_pos += x1_vel
    y1_pos += y1_vel
    x2_pos += x2_vel
    y2_pos += y2_vel

    # Boundary check fyrir báða kassana
    if 860 <= x1_pos or x1_pos <= 0:
        x1_vel *= -1
    if 440 <= y1_pos or y1_pos <= 0:
        y1_vel *= -1
    if 860 <= x2_pos or x2_pos <= 0:
        x2_vel *= -1
    if 440 <= y2_pos or y2_pos <= 0:
        y2_vel *= -1

    # Collision detection fyrir kassana, virkar bara fyrir x velocity þannig ef þeir hitta á hvorn annan að ofan eða
    # neðan verða þeir retarded
    if sq1.colliderect(sq2):
        x1_vel *= -1
        x2_vel *= -1

    # Delay til þess að hægja aðeins á þeim
    pygame.time.delay(2)
    pygame.display.update()

pygame.quit()