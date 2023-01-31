from random import randint
import data
import math

import pygame
class asteroid(object):
	def __init__(self, max_size): 
		self.max_size = max_size
		self.origin = [0,0]
		
		#the origin of the asteroid either needs to have an x value lower than 0 or higher than 640, OR a y value lower than 0 or higher than 480.
		#essentially flip a coin twice to figure out which it will be.
		offscreen_x = randint(0, 1) #if 0, start offscreen from x side, else start offscreen from y side
		offscreen_y = 0 if offscreen_x == 1 else 1 
		negative_x = 0 if offscreen_x == 1 and not randint(0,1) else 1
		negative_y = 0 if offscreen_y == 1 and not randint(0,1) else 1
		if offscreen_x:
			if negative_x:
				self.origin[0] = -20
				self.origin[1] = randint(0, data.height)
			else:
				self.origin[0] = data.width + 20
				self.origin[1] = randint(0, data.height)
		else: #offscreen_y
			if negative_y:
				self.origin[0] = randint(0, data.width)
				self.origin[1] = -20
			else:
				self.origin[0] = randint(0, data.width)
				self.origin[1] = data.height+20
		self.points = [
			[self.origin[0] + randint(-20, 20), self.origin[1] + randint(-20, 20)],
			[self.origin[0] + randint(-20, 20), self.origin[1] + randint(-20, 20)],
			[self.origin[0] + randint(-20, 20), self.origin[1] + randint(-20, 20)],
			[self.origin[0] + randint(-20, 20), self.origin[1] + randint(-20, 20)],
			[self.origin[0] + randint(-20, 20), self.origin[1] + randint(-20, 20)],
		]
		distance_x, distance_y = self.origin[0] - data.center[0], self.origin[1] - data.center[1]
		self.direction = (180 / math.pi) * -math.atan2(distance_y, distance_x) #degrees
		self.max_xv = 10
		self.max_yv = 10
		self.xv = self.max_xv * math.cos(math.radians(self.direction) + 90)
		self.yv = self.max_yv * math.sin(math.radians(self.direction) + 90)
	def move(self):
		for point in self.points:
			point[0] += self.xv
			point[1] += self.yv
		pygame.draw.polygon(data.win,(255, 255, 255), self.points)
		pygame.display.flip()

		pass
	def draw(self, surface):
		pygame.draw.polygon(data.win,(255, 255, 255), self.points)
		pygame.display.flip()
		pass