import pygame as pg
import random as r

pg.init()

screen_x_size = 800
screen_y_size = 600

screen = pg.display.set_mode((screen_x_size, screen_y_size))

pg.display.set_caption("Bouncing Ball")

ballImg = pg.image.load("Spaceship/img_downsized/ball.png")

steps_x = 0.2
steps_y = 0.2

ball_x = r.randint(0, screen_x_size)
ball_y = r.randint(0, screen_y_size)


def ball_pos(x, y):
    screen.blit(ballImg, (x, y))


isActive = True

while isActive:
    screen.fill((255, 255, 255))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            isActive = False

    if ball_x > screen_x_size - 10 or ball_x < 0:
        steps_x = -steps_x
    if ball_y > screen_y_size - 10 or ball_y < 0:
        steps_y = - steps_y

    ball_x += steps_x
    ball_y += steps_y

    ball_pos(ball_x, ball_y)

    pg.display.update()
