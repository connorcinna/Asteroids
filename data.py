import math
import pygame

width = 640 
height = 480
center = (width/2, height/2)
win = pygame.display.set_mode((width, height)) #surface
fire_event, fire_timer = pygame.USEREVENT + 1, 500



