
import pygame

import os
import random

base_path = os.path.dirname(__file__)
# dude_path = os.path.join(base_path, "dude.png")

pygame.init()

pygame.display.set_caption("Suryansh THE HERO")

# icon = pygame.image.load()
# pygame.display.set_icon(icon)

screen = pygame.display.set_mode((800, 600))

backgroundImg = pygame.image.load(os.path.join(base_path, "background.png"))

#player
playerImg = pygame.image.load(os.path.join(base_path, "ray.png"))

playerX = 367
playerY = 520
playerXChange = 0

# enemy
enemyImg = pygame.image.load(os.path.join(base_path, "shrimp.png"))
enemyX = random.randint(0, 736)
enemyY = random.randint(50, 150)
enemyXChange = 4
enemyYChange = 30

# bullet
bulletImg = pygame.image.load(os.path.join(base_path, "fishbone.png"))
bulletX = 0
bulletY = 520
bulletXChange = 0
bulletYChange = 10
bulletState = "ready"


def playerPos(xPos, yPos):
    screen.blit(playerImg, (xPos, yPos))


def enemyPos(xPos, yPos):
    screen.blit(enemyImg, (xPos, yPos))


def bulletFire(xPos, yPos):
    global bulletState
    bulletState = "fire"
    screen.blit(bulletImg, (xPos+16, yPos+10))


# Game loop
running = True

while running:
    screen.fill((0, 0, 0))
    screen.blit(backgroundImg, (0, 0))
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
             running = False

        if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_LEFT:
                 playerXChange = -5

             if event.key == pygame.K_RIGHT:
                playerXChange = 5

             if event.key == pygame.K_SPACE:
                print("f")
                bulletFire(playerX, bulletY)

        if event.type == pygame.KEYUP:
             if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                  playerXChange = 0

    playerX += playerXChange
    if playerX <=0:
        playerX = 0
    elif playerX >=736:
        playerX = 736

    playerPos(playerX, playerY)  

    enemyX += enemyXChange
    if enemyX <=0:
        enemyXChange = 4
        enemyY += enemyYChange
    elif enemyX >=736:
        enemyXChange = -4
        enemyY += enemyYChange

    if bulletState is "fire":
        bulletFire(playerX, bulletY)
        bulletY -= bulletYChange

    enemyPos(enemyX, enemyY)
    pygame.display.update()
