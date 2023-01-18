import sys
import os
import pygame
import math
import data


#several hard coded, "magic" values in this class, better practice would be to make them programmatic
class ship(object):

	def __init__(self, color, pos):
		self.color = color
		self.pos = pos 
		self.direction = 0 #a value in degrees from 0 to 360 that the ship will face based on where the mouse position is
		self.image = pygame.image.load(os.path.join("resources","ship.png"))
		self.original_image = self.image
		self.rect = self.image.get_rect()
		pass
	def turn(self, surface): #this captures the turning of the ship with the mouse
		for event in pygame.event.get():  #event loop
			if event.type == pygame.QUIT: #quit the game
				pygame.quit()
				sys.exit()

			mouse_x, mouse_y = pygame.mouse.get_pos()
			distance_x, distance_y = mouse_x - data.center[0], mouse_y - data.center[1]			
			angle = (180 / math.pi) * -math.atan2(distance_y, distance_x)
			self.image = pygame.transform.rotate(self.original_image, int(angle))
			self.rect = self.image.get_rect(center=data.center)
		
		pass
	def reset(self, pos):
		pass
	def fire_gun(self):
		pass
	def draw(self, surface): #does this need surface
		data.win.blit(self.image, (data.center[0]-25, data.center[1]-25)) #adjust for size of the ship

		pass