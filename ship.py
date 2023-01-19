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
		self.w = self.image.get_width() #25 pixels
		self.h = self.image.get_height() #25 pixels
		self.cosine = math.cos(math.radians(self.direction)+90)
		self.sine = math.sin(math.radians(self.direction)+90)
		self.head = (data.center[0]+25 + self.cosine*self.w / 2, data.center[1]-15 - self.sine*self.h / 2)
		self.original_image = self.image
		self.rotated_rect = self.image.get_rect()
		self.rotated_rect.center = data.center
		pass
	def turn(self, surface): #this captures the turning of the ship with the mouse
		for event in pygame.event.get():  #event loop
			if event.type == pygame.QUIT: #quit the game
				pygame.quit()
				sys.exit()

			mouse_x, mouse_y = pygame.mouse.get_pos()
			distance_x, distance_y = mouse_x - self.head[0], mouse_y - self.head[1]			
			self.direction = (180 / math.pi) * -math.atan2(distance_y, distance_x)
			self.image = pygame.transform.rotate(self.original_image, int(self.direction))
			self.rotated_rect = self.image.get_rect()
			self.rotated_rect.center = data.center
			self.cosine = math.cos(math.radians(self.direction)+90)
			self.sine = math.sin(math.radians(self.direction)+90)
			self.head = (data.center[0] + self.cosine*self.w / 2, data.center[1] - self.sine*self.h / 2)
			print(self.head)
		pass
	def reset(self, pos):
		pass
	def fire_gun(self):
		pass
	def draw(self, surface): #does this need surface
		data.win.blit(self.image, self.rotated_rect)

		pass