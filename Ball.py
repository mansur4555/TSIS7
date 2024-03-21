import pygame as pg

pg.init()
res = width, height = 600, 600
x = width // 2
y = height // 2
speed = 20
screen = pg.display.set_mode(res)
pg.display.set_caption("Ball Game!")
icon = pg.display.set_icon(pg.image.load('images/icon.png'))
clock = pg.time.Clock()
done = False
radius = 25
sound = pg.mixer.Sound('sounds/jump.wav')
while not done:
    pg.display.update()
    screen.fill('white')
    ball = pg.draw.circle(screen, ('red'), (x, y), radius)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT and x > radius:
                x -= speed
                sound.play()
            if event.key == pg.K_RIGHT and x < width - radius:
                x += speed
                sound.play()
            if event.key == pg.K_UP and y > radius:
                y -= speed
                sound.play()
            if event.key == pg.K_DOWN and y < height - radius:
                y += speed
                sound.play()
    clock.tick(200)