#!/usr/bin/python3
# First PyGame
#

import pygame,sys
from pygame.locals import *

game_display = pygame.display.set_mode((500,400))
pygame.display.set_caption("Game")
green = (0,255,0)
while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.quit()
  game_display.fill(green) 
  pygame.display.update()
