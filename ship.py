import sys
import os
import pygame
import math
import data 
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
	def turn(self, surface): #this captures the turning of the ship with the mouse
		mouse_x, mouse_y = pygame.mouse.get_pos()
		distance_x, distance_y = mouse_x - self.head[0], mouse_y - self.head[1]			
		self.direction = (180 / math.pi) * -math.atan2(distance_y, distance_x)
		self.image = pygame.transform.rotate(self.original_image, int(self.direction))
		self.rotated_rect = self.image.get_rect()
		self.rotated_rect.center = data.center
		self.cosine = math.cos(math.radians(self.direction)+90)
		self.sine = math.sin(math.radians(self.direction)+90)
		self.head = (data.center[0] + self.cosine*self.w / 2, data.center[1] - self.sine*self.h / 2)
	def reset(self, pos):
		pass
	def fire_gun(self, surface):
		pygame.time.delay(500) #fire every half second
		pygame.draw.line(surface, (255, 255, 255), self.head, self.head, width = 1)

	def draw(self, surface): #does this need surface
		data.win.blit(self.image, self.rotated_rect)




class bullet(object):
	
	def __init__(self, color, pos, ship):
		self.color = color
		self.pos = pos
		self.x = ship.head[0]
		self.y = ship.head[1]
		#xv and yv represent velocity of the bullet, based on the angle of head ranges from 0 to 4
		#may need to make minimum value higher
		self.xv = 0 
		self.yv = 0
		self.max_xv = 4
		self.max_yv = 4

