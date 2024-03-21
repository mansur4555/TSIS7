import pygame as pg
from datetime import datetime

pg.init()
screen = pg.display.set_mode((800, 800))
pg.display.set_caption("MickeyClock")
icon = pg.display.set_icon(pg.image.load('images/icon.png'))
clock = pg.time.Clock()
done = False
mickey = pg.image.load('images/mainclock.png')
leftarm = pg.image.load('images/leftarm.png')
rightarm = pg.image.load('images/rightarm.png')
mickey_rect = mickey.get_rect(center = (400, 400))
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    timenow = datetime.now().time()

    minangle = -(timenow.minute * 6) - 54
    secangle = -(timenow.second * 6)

    rotated_min = pg.transform.rotate(rightarm, minangle)
    rotated_sec = pg.transform.rotate(leftarm, secangle)

    right_rect = rotated_min.get_rect(center = mickey_rect.center)
    left_rect = rotated_sec.get_rect(center = mickey_rect.center)

    screen.blit(mickey, mickey_rect)
    screen.blit(rotated_min, right_rect)
    screen.blit(rotated_sec, left_rect)

    pg.display.flip()
    clock.tick(60)