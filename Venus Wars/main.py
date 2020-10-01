import pygame
import random
import math
pygame.init()
window = pygame.display.set_mode((800, 750))
pygame.display.set_caption('Venus Wars')
icon = pygame.image.load('venus.png')
pygame.display.set_icon(icon)
background = pygame.image.load('rsz_892.png')
playerImg = pygame.image.load('rocket.png')
playerX = 370
playerY = 580
playerX_change = 0
score_value = 0
font = pygame.font.SysFont('freesansbold.tff', 50)
textX=320
textY=5
def show_score(x,y):
    score=font.render("Score : "+str(score_value),True,(0,255,225))
    window.blit(score,(x,y))
def player(x, y):
    window.blit(playerImg, (x, y))
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 580
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"
def bullet_fire(x, y):
    global bullet_state
    bullet_state = "fire"
    window.blit(bulletImg, (x + 16, y + 10))
def hit(enemyX, enemyY, bulletX, bulletY):
    a = math.pow(enemyX - bulletX, 2)
    b = math.pow(enemyY - bulletY, 2)
    space = math.sqrt(a + b)
    if space < 27:
        return True
    else:
        return False
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 736)
enemyY = random.randint(80, 250)
enemyX_change = 4
enemyY_change = 20
def enemy(x, y):
    window.blit(enemyImg, (x, y))
running = True
while running:
    window.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerX_change = 8
            if event.key == pygame.K_LEFT:
                playerX_change = -8
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    bullet_fire(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerX_change = 0
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736
    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 4
        enemyY += enemyY_change
    if enemyX >= 736:
        enemyX_change = -4
        enemyY += enemyY_change
    if enemyY >= 670:
        enemyY_change = 0
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        bullet_fire(bulletX, bulletY)
        bulletY -= bulletY_change
    isHit = hit(enemyX, enemyY, bulletX, bulletY)
    if isHit:
        bulletY = 580
        bullet_state = "ready"
        score_value += 1
        print(score_value)
        enemyX = random.randint(0, 736)
        enemyY = random.randint(80, 250)
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    show_score(textX, textY)
    pygame.display.update()
