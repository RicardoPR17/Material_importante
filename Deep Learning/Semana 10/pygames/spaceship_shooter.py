import pygame
import random as r
import math
from pygame import mixer

mixer.init()
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('space shooter game')

mixer.music.load("Spaceship/Sounds/game.mp3")
mixer.music.play(-1)  # Música en bucle

icon_img = pygame.image.load("Spaceship/img_downsized/icon.png")
ball_img = pygame.image.load("Spaceship/img_downsized/ball.png")
bullet_img = pygame.image.load("Spaceship/img_downsized/bullet_d.png")
enemy1_img = pygame.image.load("Spaceship/img_downsized/enemy1_d.png")
enemy2_img = pygame.image.load("Spaceship/img_downsized/enemy2_d.png")
player_img = pygame.image.load("Spaceship/img_downsized/player_d.png")
space_bg_img = pygame.image.load("Spaceship/img_downsized/space_d.png")
alien_blaster_img = pygame.image.load("Spaceship/img_downsized/alienblaster_d.png")
explosion_img = pygame.image.load("Spaceship/img_downsized/explosion.png")

font = pygame.font.SysFont("Ariel", 32, 'bold')

pygame.display.set_icon(icon_img)


spaceshipX = 370
spaceshipY = 480
changeX = 0
changeY = 0
ratio = 0.1

enemy1X = r.randint(0, 736)
enemy1Y = 50
enemy1_changeX = 1
enemy1_changeY = 0
enemy1_ratio = 0.1

bulletX = 370
bulletY = 480
bullet_changeY = 1
bullet_ratio = 0.1
check = False

score = 0


def player():
    screen.blit(player_img, (spaceshipX, spaceshipY))


def enemy1():
    screen.blit(enemy1_img, (enemy1X, enemy1Y))


def bullet():
    screen.blit(bullet_img, (bulletX, bulletY))


def explosion():
    screen.blit(explosion_img, (enemy1X + 10, enemy1Y))


def collision():
    distance = math.sqrt(math.pow(bulletX - enemy1X + 10, 2) + math.pow(bulletY - enemy1Y, 2))
    if distance < 55:
        return True


def score_text():
    img = font.render(f'Score: {score}', True, 'white')
    screen.blit(img, (10, 10))


running = True
while running:
    screen.blit(space_bg_img, (0, 0))  # Top corner
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                changeX = -1 * ratio
            if event.key == pygame.K_RIGHT:
                changeX = +1 * ratio
            if event.key == pygame.K_UP:
                changeY = -1 * ratio
            if event.key == pygame.K_DOWN:
                changeY = +1 * ratio
            if event.key == pygame.K_SPACE:
                if not check:
                    bullet_sound = mixer.Sound("Spaceship/Sounds/rocket.wav")
                    bullet_sound.play()
                    check = True
                    bulletX = spaceshipX + 22
                    bulletY = spaceshipY

        if event.type == pygame.KEYUP:
            changeX = 0
            changeY = 0

    spaceshipX += changeX
    spaceshipY += changeY

    if spaceshipX < 0:
        spaceshipX = 0
    elif spaceshipX > 736:
        spaceshipX = 736
    if spaceshipY > 480:
        spaceshipY = 480
    elif spaceshipY < 30:
        spaceshipY = 30

    enemy1X += enemy1_changeX * enemy1_ratio
    enemy1Y += enemy1_changeY

    if enemy1X < 0 or enemy1X > 726:
        enemy1_ratio *= -1
        enemy1Y += 20

    if enemy1Y > 480:
        enemy1Y = 480
    elif enemy1Y < 30:
        enemy1Y = 30

    if bulletY < 0:
        check = False

    if check:
        bulletY -= bullet_changeY * bullet_ratio
        bullet()

    collided = collision()

    enemy1()

    if collided:
        hit_sound = mixer.Sound("Spaceship/Sounds/hit.wav")
        hit_sound.play()
        explosion()
        check = False
        enemy1X = r.randint(0, 736)
        enemy1Y = 50
        enemy1()
        score += 1

    player()
    score_text()

    pygame.display.update()
