
try:
    import pygame_sdl2
    pygame_sdl2.import_as_pygame() 
except ImportError:
    pass

import pygame

from pygame import mixer
import os
import random
import math

base_path = os.path.dirname(__file__)
# dude_path = os.path.join(base_path, "dude.png")

pygame.init()

pygame.display.set_caption("Suryansh THE HERO")

# icon = pygame.image.load()
# pygame.display.set_icon(icon)

screen = pygame.display.set_mode((800, 600))



backgroundImg = pygame.image.load(os.path.join(base_path, "background.png"))

# music
mixer.music.load(os.path.join(base_path, "background.wav"))
mixer.music.play(-1)

 

# score
score=0
font= pygame.font.Font("freesansbold.ttf",32)
fontX=10
fontY=20

fontGameEnd= pygame.font.Font("freesansbold.ttf",32)
fontGameOverX=350
fontGameOverY=300

#player
playerImg = pygame.image.load(os.path.join(base_path, "ray.png"))

playerX = 367
playerY = 520
playerXChange = 0

# enemy

enemyImg = []
enemyX = []
enemyY = []
enemyXChange =[]
enemyYChange = []
numOfEnemies=5

for  i in range (numOfEnemies):
    enemyImg.append(pygame.image.load(os.path.join(base_path, "shrimp.png")))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyXChange.append(4)
    enemyYChange.append(30)
print(enemyImg)

# bullet
bulletImg = pygame.image.load(os.path.join(base_path, "fishbone.png"))
bulletX = 0
bulletY = 520
bulletXChange = 0
bulletYChange = 10
bulletState = "ready"


def showScore(xPos, yPos):
   scoreValue= font.render("Score : "+str(score),True,(255,255,255))
   screen.blit(scoreValue, (xPos, yPos))

def showGameOver(xPos, yPos):
   gameOverValue= font.render("Game Over",True,(255,255,255))
   screen.blit(gameOverValue, (xPos, yPos))

def playerPos(xPos, yPos):
    screen.blit(playerImg, (xPos, yPos))


def enemyPos(xPos, yPos,i):
    screen.blit(enemyImg[i], (xPos, yPos))


def bulletFire(xPos, yPos):
    global bulletState
    bulletState = "fire"
    screen.blit(bulletImg, (xPos+16, yPos+10))

def isCollision(enemyX,enemyY, bulletX,bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX,2)+ math.pow(enemyY-bulletY,2))
    if distance <20:
        return True
    else:
        return False



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
                if bulletState is "ready":
                    bulletSound= mixer.Sound(os.path.join(base_path, "laser.wav"))
                    bulletSound.play()
                    bulletX =playerX
                    bulletFire(bulletX, bulletY)

        if event.type == pygame.KEYUP:
             if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                  playerXChange = 0

    playerX += playerXChange
    if playerX <=0:
        playerX = 0
    elif playerX >=736:
        playerX = 736

    playerPos(playerX, playerY)  

    for  i in range (numOfEnemies):
        if enemyY[i] >= 480:
            for j in range(numOfEnemies):
                enemyY[j]=2000

            showGameOver(fontGameOverX,fontGameOverY)
            break


        enemyX[i] += enemyXChange[i]
        if enemyX[i] <=0:
            enemyXChange[i] = 4
            enemyY[i] += enemyYChange[i]
        elif enemyX[i] >=736:
            enemyXChange[i] = -4
            enemyY[i] += enemyYChange[i]
        
        collision = isCollision(enemyX[i],enemyY[i], bulletX,bulletY)

        if collision:
            explosionSound= mixer.Sound(os.path.join(base_path, "explosion.wav"))
            explosionSound.play()
            bulletY=520
            bulletState="ready"
            score +=1
            enemyX[i]= random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)
        
        enemyPos(enemyX[i], enemyY[i], i)

    if bulletY <= 0:
            bulletY=520
            bulletState="ready"

    if bulletState is "fire":
            bulletFire(bulletX, bulletY)
            bulletY -= bulletYChange

    

    showScore(fontX,fontY)
    pygame.display.update()
