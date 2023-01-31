import math
import pygame
import ship
import asteroid as ast
import data
import tkinter as tk
from random import randint
from tkinter import messagebox


player_ship = ship.ship(data.center)

def redrawWindow(surface):
	surface.fill((0,0,0))
	player_ship.draw(surface)
	#asteroid.draw(surface)
	pygame.display.update()


def message_box(subject, content):
	pass


def main():
	
	pygame.time.set_timer(data.fire_event, data.fire_timer)
	flag = True
	clock = pygame.time.Clock() 
	bullets = []
	asteroids = []
	while flag: #main game loop
		for event in pygame.event.get():  #event loop
			if event.type == pygame.QUIT: #quit the game
				pygame.quit()
				sys.exit()
			if event.type == data.fire_event: #every 500 ms
				#construct a bullet object every fire_event and add to bullets array
				bullets.append(ship.bullet(data.win, player_ship)) 
			if event.type == data.asteroid_event: #every 250 ms
				#same process as bullets
				max_size = randint(5, 20)
				asteroids.append(ast.asteroid(max_size))

		for bullet in bullets:
			bullet.move()	

		for asteroid in asteroids:
			asteroid.move()	

		player_ship.turn(data.win) #captures the event loop
		#time.delay pauses the program for a time in milliseconds, unsure if this and clock.tick are both needed
		pygame.time.delay(50)  
		#clock.tick called once per frame, time is in milliseconds, the argument will delay the game to force it to run at 10 frames per second
		clock.tick(10) 
		redrawWindow(data.win) #update frame





main()
