import pygame


def text_to_screen(screen, text, x, y, size=50, color=(200, 000, 000), font_type='helvetica'):
    try:
        text = str(text)
        font = pygame.font.SysFont(font_type, size)
        text = font.render(text, True, color)
        screen.blit(text, (x, y))

    except:
        print('Font Error, saw it coming')
        raise
