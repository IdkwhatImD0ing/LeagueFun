import pygame
import math
from pygame.locals import *

pygame.init()
width, height = 1920, 1080
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

player = pygame.image.load("src\images\icon.png")
player = pygame.transform.scale(player, (50, 50))
playerPos = [1920/2, 1080/2]
background = pygame.image.load("src\images\\tempBackground.jpg")

positionReached = True
futurePosition = [0, 0]
angle = 0


while True:
    screen.fill(0)
    screen.blit(background, (0,0))
    screen.blit(player, (playerPos[0] - 25, playerPos[1] - 25))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            positionReached = False
            futurePosition[0], futurePosition[1] = pygame.mouse.get_pos()
            print(futurePosition[0], futurePosition[1])
            x = futurePosition[0] - playerPos[0]
            y = futurePosition[1] - playerPos[1]
            angle = math.atan2(y, x)
    if(positionReached == False):
        playerPos[0] += 10 * math.cos(angle)
        playerPos[1] += 10 * math.sin(angle)
        if abs(playerPos[0]- futurePosition[0]) < 5 and abs(playerPos[1] - futurePosition[1]) < 5:
            positionReached = True
    clock.tick(60)


