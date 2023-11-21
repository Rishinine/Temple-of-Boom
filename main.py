#important imports
import pygame as pg
import ctypes
import os

#pygame setup 
user32 = ctypes.windll.user32
pg.init()
screen = pg.display.set_mode((user32.GetSystemMetrics(0)-200,user32.GetSystemMetrics(1)-200))
running = True
clock = pg.time.Clock()
block = pg.image.load(os.path.join('Assets','brick.png'))
block = pg.transform.scale(block, (100, 25))
x=0
r=255
g=255
b=255
while running:
    for envent in pg.event.get():
        if envent.type == pg.QUIT:
            running = False
    pg.Surface.fill(screen,(r,g,b))
    pg.Surface.blit(screen,block,(x,50))
    pg.display.flip()
    clock.tick(60)

pg.quit()    