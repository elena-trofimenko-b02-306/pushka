import pygame as pg
import sys
pg.init()
screen = pg.display.set_mode((800,800))
r = pg.Rect(300,300,100,200)
pg.draw.rect(screen,(0,0,100),r,60)
pg.draw.line(screen,(240,0,100),(0,0),(100,300),3)
pg.draw.circle(screen,(0,100,250),(300,200),40,5)
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    pg.display.flip()