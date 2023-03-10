import sys
import os
import pygame
import math
import data 
class ship(object):

	def __init__(self, pos):
		self.pos = pos
		self.direction = 0 #a value in degrees from 0 to 360 that the ship will face based on where the mouse position is
		self.image = pygame.image.load(os.path.join("resources","ship.png"))
		self.w = self.image.get_width() #50 pixels
		self.h = self.image.get_height() #50 pixels
		self.cosine = math.cos(math.radians(self.direction)+90)
		self.sine = math.sin(math.radians(self.direction)+90)
		print("self.cosine: {}".format(self.cosine))
		print("self.sine: {}".format(self.sine))
		self.head = (data.center[0] + (self.cosine*self.w) / 2, data.center[1] - (self.sine*self.h / 2))
		self.init_flag = False
		self.original_image = self.image
		self.rotated_rect = self.image.get_rect()
		self.rotated_rect.center = data.center
	def turn(self, surface): #this captures the turning of the ship with the mouse)
		mouse_x, mouse_y = 0, 0
		if not self.init_flag:
			self.init_flag = True
			mouse_x, mouse_y = self.head[0], self.head[1]
		else:
			mouse_x, mouse_y = pygame.mouse.get_pos()
		distance_x, distance_y = mouse_x - self.head[0], mouse_y - self.head[1]			
		self.direction = (180 / math.pi) * -math.atan2(distance_y, distance_x) #degrees
		self.image = pygame.transform.rotate(self.original_image, int(self.direction))
		self.rotated_rect = self.image.get_rect()
		self.rotated_rect.center = data.center
		self.cosine = math.cos(math.radians(self.direction)+90)
		self.sine = math.sin(math.radians(self.direction)+90)
		print("self.cosine: {}, self.sine: {} ".format(self.cosine, self.sine))
		self.head = (data.center[0] + (self.cosine*self.w / 2), data.center[1] - (self.sine*self.h / 2))
		surface.set_at((int(self.head[0]), int(self.head[1])), (255, 255, 255))
		pygame.display.flip()
	def reset(self, pos):
		pass

	def draw(self, surface): #does this need surface
		data.win.blit(self.image, self.rotated_rect)


class bullet(object):
	
	def __init__(self, surface, ship):
		self.x = ship.head[0]
		self.y = ship.head[1]
		#xv and yv represent velocity of the bullet, based on the angle of head ranges from 0 to max_xv 
		self.max_xv = 15 
		self.max_yv = 15 
		self.xv = self.max_xv * math.cos(math.radians(ship.direction)+90)
		self.yv = self.max_yv * math.sin(math.radians(ship.direction)+90)
		#print("xv: {} yv: {}".format(self.xv, self.yv))
		#print("x: {} y: {}".format(self.x, self.y))

		#when a bullet is constructed, draw it at the head of the ship
		surface.set_at((int(self.x), int(self.y)), (255, 255, 255))
		pygame.display.flip()

	def move(self):
		self.x += self.xv 
		self.y += self.yv 
		data.win.set_at((int(self.x), int(self.y)), (255, 255, 255))
		pygame.display.flip() 