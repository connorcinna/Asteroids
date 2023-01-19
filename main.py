import math
import random
import pygame
import ship
import asteroid
import data
import tkinter as tk
from tkinter import messagebox


player_ship = ship.ship((255, 255, 255),data.center)#maybe move this to data

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
	
	flag = True
	clock = pygame.time.Clock() 
	while flag: #main game loop
		for event in pygame.event.get():  #event loop
			if event.type == pygame.QUIT: #quit the game
				pygame.quit()
				sys.exit()
			if event.type == data.fire_event:
				#pygame.time.set_timer()
				pass

		player_ship.turn(data.win) #captures the event loop
		#player_ship.fire_gun(data.win)
		#time.delay pauses the program for a time in milliseconds, unsure if this and clock.tick are both needed
		pygame.time.delay(50)  
		#clock.tick called once per frame, time is in milliseconds, the argument will delay the game to force it to run at 10 frames per second
		clock.tick(10) 
		redrawWindow(data.win) #update frame





main()
