# Hannes Árni Hannesson, 27/08/18
# Teiknar tening á miðju skjásins
import pygame

pygame.init()

BACKGROUND_COLOR = (1, 22, 39)
WINDOW_SIZE = (640, 480)

# Loadum mynd, pathið er argumentið
image = pygame.image.load('images/Teningur5.png')


window = pygame.display.set_mode(WINDOW_SIZE)
window.fill(BACKGROUND_COLOR)
pygame.display.set_caption("Verkefni 1a 2, K2")

running = True

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False

    # Brykkjum myndinni sem við calluðum uppi á skjáinn,
    # 270x190 border til þess að teningurinn sé í miðjunni, miðað við að hann sé 100x100
    window.blit(image, (270, 190))

    pygame.display.update()

pygame.quit()