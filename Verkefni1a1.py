# Hannes Árni Hannesson, 27/08/18
# Forrit sem sýnir bara 3 ferhyrninga og 2 hringi
import pygame

# Byrjum keyrslu á pygame
pygame.init()

# Definum alla liti sem við ætlum að nota, í rgb formatti.
BACKGROUND_COLOR = (1, 22, 39)
RED = (130, 9, 51)
ORANGE = (237, 106, 90)
YELLOW = (242, 243, 174)
WHITE = (239, 233, 231)
BLUE = (34, 116, 165)

WINDOW_SIZE = (640, 480)

# Búum til glugga sem er með stærðina 640px X 480px
window = pygame.display.set_mode(WINDOW_SIZE)
# Fyllum skjáinn með litnum BACKGROUND_COLOR
window.fill(BACKGROUND_COLOR)
# Breytum heitinu á glugganum
pygame.display.set_caption("Verkefni 1a 1, K2")

# Segjum að forritið sé að keyra
running = True

while running:
    # Essentially styttum bara setninguna, með því að setja það í annan variable.
    event = pygame.event.poll()
    # Tékkum hvort ýtt sé á exit
    if event.type == pygame.QUIT:
        # Segjum while lykkjunni að hætta að keyra
        running = False
    # Tékkum hvort í fyrsta lagi sé verið að ýta á einhvern takka, og ef svo er, hvort það sé escape
    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        running = False

    # Teiknum fyrst 3 kassa í röð, allir 20 px border frá toppnum og alltaf 20 px border á milli
    # Þeir notast við liti defined above. Stærðir eru síðustu tvö arguments í pygame.Rect()
    pygame.draw.rect(window, RED, pygame.Rect(20, 20, 50, 50))
    pygame.draw.rect(window, ORANGE, pygame.Rect(90, 20, 70, 90))
    pygame.draw.rect(window, YELLOW, pygame.Rect(180, 20, 35, 140))

    # Núna teiknum við tvo hringi, með mismunani liti, og hnitin að miðjunni eru inni í sviganum
    # Siðasta argument er radíus hringsins.
    pygame.draw.circle(window, WHITE, (290, 75), 55)
    pygame.draw.circle(window, BLUE, (465, 120), 100)

    # Updateum það sem sést á skjánum
    pygame.display.update()

# Lokum forritinu
pygame.quit()