import pygame
import random
from color_library import *

pygame.init()


# If we want to use sprites we create a class that inherits from the Sprite class.
# Each class has an associated image and a rectangle.
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Player(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos


class Missile(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = missile_image
        self.rect = self.image.get_rect()


# Lets load the game images and put them into variables
player_image = pygame.image.load('Images3/player_pad.png')
enemy_image = pygame.image.load('Images3/green_ball.png')
missile_image = pygame.image.load('Images3/missile.png')

SCREEN_SIZE = (300, 600)
screen = pygame.display.set_mode(SCREEN_SIZE)

# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
asteroid_list = pygame.sprite.Group()
# Group to hold missiles
missile_list = pygame.sprite.Group()
# This is a list of every sprite.
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()

# Makes 8 enemies 
for i in range(8):
    enemies = Enemy(random.randrange(20, 280, 18), random.randrange(0, 40, 18))
    asteroid_list.add(enemies)
    all_sprites_list.add(enemies)

# Create a player block
player = Player(150, 580)
all_sprites_list.add(player)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
score = 0

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shot = Missile()
                shot.rect.x = player.rect.x + 30
                shot.rect.y = player.rect.y - 15
                missile_list.add(shot)
                all_sprites_list.add(shot)

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        if player.rect.x < -60:
            player.rect.x = 700
        player.rect.x -= 5
    elif key[pygame.K_RIGHT]:
        if player.rect.x > 700:
            player.rect.x = - 60
        player.rect.x += 5

    screen.fill(BLACK)

    # See if the player block has collided with anything.
    pygame.sprite.groupcollide(missile_list, asteroid_list, True, True)

    # Missiles move at a constant speed up the screen, towards the enemy
    for shot in missile_list:
        shot.rect.y -= 5

    # All the enemies move down the screen at a constant speed
    for block in asteroid_list:
        block.rect.y += 1

    # Draw all the spites
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(50)

pygame.quit()
