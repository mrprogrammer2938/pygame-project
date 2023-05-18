#!/usr/bin/python3
# Cat Game
# Write By Sina Meysami

import pygame,sys
from pygame.locals import *

pygame.init()
FPS = 30
clock = pygame.time.Clock()
display_game = pygame.display.set_mode((400,300),0,32)
pygame.display.set_caption("Cat Game")
white = (255,255,255)

catImg = pygame.image.load("cat.png")
catx = 10
caty = 10
direction = 'right'
while True:
    display_game.fill(white)
    pygame.display.set_icon(catImg)
    
    if direction == 'right':
        catx += 5
        if catx == 280:
            direction = 'down'
    elif direction == 'down':
        caty += 5
        if caty == 220:
            direction = 'left'
    elif direction == 'left':
        catx -= 5
        if catx == 10:
            direction = 'up'
    elif direction == 'up':
        caty -= 5
        if caty == 10:
            direction = 'right'
    
    display_game.blit(catImg,(catx,caty))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

    clock.tick(FPS)
