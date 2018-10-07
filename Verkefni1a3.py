# Hannes Árni Hannesson, 27/08/18
# teiknum takka, og texta á takkann
import pygame

pygame.init()

BACKGROUND_COLOR = (255, 255, 255)
BLUE = (34, 116, 165)
WINDOW_SIZE = (640, 480)

my_font = pygame.font.SysFont('DroidSans', 50)

window = pygame.display.set_mode(WINDOW_SIZE)
window.fill(BACKGROUND_COLOR)
pygame.display.set_caption("Verkefni 1a 2, K2")

running = True

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False

    x_pos, y_pos = 195, 165
    pygame.draw.rect(window, BLUE, pygame.Rect(x_pos, y_pos, 250, 150))
    window.blit(my_font.render("Press me!", 1, BACKGROUND_COLOR), (x_pos+45, y_pos+55))


    pygame.display.update()

pygame.quit()