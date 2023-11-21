#important imports
import pygame as pg

#pygame setup 
pg.init()
screen = pg.display.set_mode((1280,720))
running = True
clock = pg.time.Clock()

while running:
    for envent in pg.event.get():
        if envent.type == pg.QUIT:
            running = False
    pg.display.flip()
    clock.tick(60)
pg.quit()    