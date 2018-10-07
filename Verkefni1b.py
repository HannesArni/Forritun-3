# Hannes Árni Hannesson, 27/08/18
# Teningsleikur þar sem keppt er við tölvuna. Super leiðinlegur bara.
import pygame
import random
from dice_thrower import DiceThrower


# Sýnir dice myndirnar í röð, í miðju skjásins. Tekur inn listann sem verið er að vinna með (len(listi)) = 5
# og y_pos sem er hvar röðin kemur
def dice_row(number_list, y_pos):
    x_pos = 480 - ((5 * 120) - 20) / 2
    for image in number_list:
        window.blit(image_list[image], (x_pos, y_pos))
        x_pos += 120


comp_list = DiceThrower()

user_list = DiceThrower()

# Step er notað til þess að segja forritinu hvar í leiknum notandi er.
# step = 1: Hægt er að ýta á kasta
# Step = 2: Hægt er að annaðhvort kasta aftur fyrir notanda eða sýna eina
# Step = 3: Búið að velja annaðhvort í step 2 og sýna þarf trophy, Bara hægt að ýta á restart
step = 1

pygame.init()

# Litir og window size
CASINO_GREEN = (7, 100, 36)
WINDOW_SIZE = (960, 540)
GREY = (171, 169, 191)
DARK_GREY = (109, 108, 122)

image_list = []
# Köllum á allar teningsmyndirnar í imges möppunni og geymum í image_list trophy fyrir neðan
for x in range(7):
    image_list.append(pygame.image.load('images/Teningur' + str(x) + '.png'))
trophy = pygame.image.load('images/Trophy.png')

window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Verkefni 1a 2, K2")
window.fill(CASINO_GREEN)

my_font = pygame.font.SysFont('arialblack', 20)

running = True

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = False
    window.fill(CASINO_GREEN)
    # Sýnum efri röðina
    dice_row(comp_list.dice_list, 50)
    # Sýnum neðri röðina
    dice_row(user_list.dice_list, 200)

    # Teiknum 3 takka með textanum í listanum hérna fyrir neðan inní respectively. x og y fyrsta takka er hægt að breyta
    text_list = ["SPILA", "KASTA", " SÝNA"]
    button_list = []
    button_y_pos = 350
    button_x_pos = 230
    for x in range(3):
        button_list.append(pygame.draw.rect(window, GREY, pygame.Rect(button_x_pos, button_y_pos, 150, 80)))
        window.blit(my_font.render(text_list[x], 1, CASINO_GREEN), (button_x_pos + 35, button_y_pos + 25))
        button_x_pos += 175

    # Teiknum neðsta kassann
    pygame.draw.rect(window, DARK_GREY, pygame.Rect(405, button_y_pos + 100, 150, 80))
    button_list.append(window.blit(my_font.render("NÝR LEIKUR", 1, CASINO_GREEN), (410, button_y_pos + 125)))

    # Tékkum hvort ýtt er á einhvern takka í listanum, og hvort step sé rétt fyrir viðeigandi takka.
    if event.type == pygame.MOUSEBUTTONDOWN:
        for i in range(len(button_list)):
            if button_list[i].collidepoint(event.pos):
                if i == 0 and step == 1:
                    user_list.throw()
                    comp_list.throw()
                    user_list.dice_list[4] = 0
                    step = 2
                elif i == 1 and step == 2:
                    user_list.rethrow([0, 1, 2, 3, 4])
                    step = 3
                elif i == 2 and step == 2:
                    user_list.dice_list[4] = random.randint(1, 6)
                    step = 3
                elif i == 3 and step == 3:
                    user_list.dice_list = [0, 0, 0, 0, 0]
                    comp_list.dice_list = [0, 0, 0, 0, 0]
                    step = 1

    # Ef leikurinn klárast, þegar step er 3, mun setja trophy-ið á skjáinn
    if step == 3:
        if sum(user_list.dice_list) < sum(comp_list.dice_list):
            window.blit(trophy, (800, 75))
        elif sum(user_list.dice_list) > sum(comp_list.dice_list):
            window.blit(trophy, (800, 225))
        elif sum(user_list.dice_list) == sum(comp_list.dice_list):
            print(sum(user_list.dice_list), sum(comp_list.dice_list))
            window.blit(trophy, (800, 125))

    pygame.display.update()

pygame.quit()
