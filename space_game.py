import pygame, controls

from pygame.sprite import Group
from ginn import Gun
from stats import Stats




def run():
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("Космические защитники")
    bg_color = (0, 0, 0)
    ginn = Gun(screen)
    bullets = Group()
    inos = Group()
    controls.create_army(screen, inos)
    stats = Stats()


    while True:
        controls.events(screen, ginn, bullets)
        ginn.update_up()
        controls.update(bg_color, screen, ginn, inos, bullets)
        controls.update_bulleta(screen,  inos, bullets)
        controls.update_inos(stats, screen, ginn, inos, bullets)


run()
