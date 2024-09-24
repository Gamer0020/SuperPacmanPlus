import pygame as pg

pg.init()
screen = pg.display.set_mode((800, 600))
HEIGHT = 600
WIDTH = 800

image = pg.image.load("./images/Pacman.svg")
image = pg.transform.scale(image, (100, 100))
imagelocation = [0, 0]
imagerotation = 90



running = True
while running:
    screen.fill(pg.Color(0, 0, 0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                imagelocation[0] -= 100
                image = pg.transform.rotate(image, imagerotation-270)
                imagerotation = 270

            if event.key == pg.K_RIGHT:
                imagelocation[0] += 100
                image = pg.transform.rotate(image, imagerotation-90)
                imagerotation = 90

            if event.key == pg.K_DOWN:
                imagelocation[1] += 100
                image = pg.transform.rotate(image, imagerotation-180)
                imagerotation = 180

            if event.key == pg.K_UP:
                imagelocation[1] -= 100
                image = pg.transform.rotate(image, imagerotation)
                imagerotation = 0

    screen.blit(image, pg.Rect(imagelocation[0], imagelocation[1], 200, 200))
    for i in range(5):
        for j in range(8):
            pg.draw.circle(screen, pg.color.Color(200, 200, 200), (i*100+50, j*100+50), 10)
    pg.display.update()

pg.quit()