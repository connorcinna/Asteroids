import math
import random
import pygame
import ship
import asteroid
import data
import tkinter as tk
from tkinter import messagebox


player_ship = ship.ship((255, 255, 255),data.center)

def redrawWindow(surface):
	surface.fill((0,0,0))
	player_ship.draw(surface)
	#asteroid.draw(surface)
	pygame.display.update()


def spawn_asteroid():
	pass

def message_box(subject, content):
	pass


def main():
	
	pygame.time.set_timer(data.fire_event, data.fire_timer)
	flag = True
	clock = pygame.time.Clock() 
	bullets = []
	while flag: #main game loop
		for event in pygame.event.get():  #event loop
			if event.type == pygame.QUIT: #quit the game
				pygame.quit()
				sys.exit()
			if event.type == data.fire_event:
				#construct a bullet object every fire_event and add to bullets array
				bullets.append(ship.bullet(data.win,player_ship.head, player_ship)) 
				pass
		for bullet in bullets:
			bullet.x += bullet.xv 
			bullet.y += bullet.yv 
			#pygame.draw.line(data.win, (255,255,255), (bullet.x, bullet.y), (bullet.x, bullet.y), width = 1)
			data.win.set_at((int(bullet.x), int(bullet.y)), (255, 255, 255))
			pygame.display.flip()


		player_ship.turn(data.win) #captures the event loop
		#time.delay pauses the program for a time in milliseconds, unsure if this and clock.tick are both needed
		pygame.time.delay(50)  
		#clock.tick called once per frame, time is in milliseconds, the argument will delay the game to force it to run at 10 frames per second
		clock.tick(10) 
		redrawWindow(data.win) #update frame





main()
