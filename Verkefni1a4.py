# coding=UTF-8
# Hannes Árni Hannesson, 27/08/18
# Teiknar þrjá teningar á miðju skjásins
import pygame

pygame.init()

BACKGROUND_COLOR = (1, 22, 39)
WINDOW_SIZE = (640, 480)

# Búum til tóman lista þar sem myndirnar verða geymdar
image_list = []
# Keyrum lykkjuna þrisvar, og bætum mynd við listann sem er í images möppunni sem á að vera á sama stað og þetta forrit.
# inni í images, ætti að vera nokkrar .png myndir sem heita Teningur 0-6,
# Við köllum á þrjár af þeim og setjum í listann okkar.
for x in range(3):
    image_list.append(pygame.image.load('images/Teningur'+ str(x+1)+ '.png'))


window = pygame.display.set_mode(WINDOW_SIZE)
window.fill(BACKGROUND_COLOR)
pygame.display.set_caption("Verkefni 1a 2, K2")

running = True

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False

    # Declarum byrjunarposition, höfum þessa stærðfræðijöfnu til þess að teningarnir séu alltaf í miðju skjásins
    x_pos = 320- ((len(image_list)*120)-20)/2
    # Förum í gegnum myndirnar sem eru í listanum
    for image in image_list:
        # Sýnum myndina
        window.blit(image, (x_pos, 190))
        x_pos += 120

    pygame.display.update()

pygame.quit()