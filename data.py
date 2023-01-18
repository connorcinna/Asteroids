import math
import pygame

width = 640 
height = 480
center = (width/2, height/2)
win = pygame.display.set_mode((width, height)) #surface

#for rotating a single point, specifically for rotating the 3 points that make up ship
#accepts a tuple of a single point
#returns a tuple of the rotated point
def rotate(point, angle, radius): 
	x = center[0] + radius * math.cos(point[0] + angle)
	y = center[1] + radius * math.sin(point[1] + angle) 
	print([x,y])
	return [x, y]
