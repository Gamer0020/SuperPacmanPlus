import pygame as pg

pg.init()
screen = pg.display.set_mode((800, 600))
HEIGHT = 600
WIDTH = 800

image = pg.image.load("./images/Pacman.svg")
image = pg.transform.scale(image, (100, 100))
imagelocation = [0, 0]
imagerotation = 90

listepoints = [[True for i in range(6)] for i in range(8)]

running = True
while running:
    screen.fill(pg.Color(0, 0, 0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                if imagelocation[0] -100 >= 0:
                    imagelocation[0] -= 100
                image = pg.transform.rotate(image, imagerotation-270)
                imagerotation = 270

            if event.key == pg.K_RIGHT:
                if imagelocation[0] + 100 < WIDTH:
                    imagelocation[0] += 100
                image = pg.transform.rotate(image, imagerotation-90)
                imagerotation = 90

            if event.key == pg.K_DOWN:
                if imagelocation[1] + 100 < HEIGHT:
                    imagelocation[1] += 100
                image = pg.transform.rotate(image, imagerotation-180)
                imagerotation = 180

            if event.key == pg.K_UP:
                if imagelocation[1] - 100 >= 0:
                    imagelocation[1] -= 100
                image = pg.transform.rotate(image, imagerotation)
                imagerotation = 0
            
            if event.key == pg.K_SPACE:
                for i in range(8):
                    for j in range(6):
                        listepoints[i][j] = True
    x, y = imagelocation
    x //= 100
    y //= 100
    listepoints[x][y] = False

    for i in range(8):
        for j in range(6):
            if listepoints[i][j]:
                pg.draw.circle(screen, pg.color.Color(200, 200, 200), (i*100+50, j*100+50), 10)
                foundthing = True

    screen.blit(image, pg.Rect(imagelocation[0], imagelocation[1], 200, 200))
    pg.display.update()

pg.quit()