# Hannes Árni Hannesson, 27/08/18
# Setur random tening á miðju skjásins
import pygame
import random

pygame.init()

WINDOW_SIZE = (640, 480)

# Búum til tóman lista þar sem myndirnar verða geymdar
image_list = []
# Keyrum lykkjuna þrisvar, og bætum mynd við listann sem er í images möppunni sem á að vera á sama stað og þetta forrit.
# inni í images, ætti að vera nokkrar .png myndir sem heita Teningur 0-6,
# Við köllum á þrjár af þeim og setjum í listann okkar.
for x in range(6):
    image_list.append(pygame.image.load('images/Teningur'+ str(x+1)+ '.png'))
# Veljum random mynd úr listanum búinn til fyrir ofan, og setjum hana í image variableinn
image = random.choice(image_list)


window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Verkefni 1a 2, K2")

# Loadum mynd sem geymd er í bakgrunnur variable, krefst images möppu með eftirfarandi mynd í.
bakgrunnur = pygame.image.load("images/Playing_board_background.png")
window.blit(bakgrunnur, (0,0))

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