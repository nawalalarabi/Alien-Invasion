import pygame
import settings
import ship
import game_functions as GF
from pygame.sprite import Group
def run_game():
	#@ai_stngs : Alien Invaders Settings
	ai_stngs = settings.Settings()

	# Initialize game and create a screen object.
	pygame.init()

	#game icon
	ai_stngs.ai_icon("images/alien.bmp")

	#build screen
	screen = ai_stngs.ai_screen_size()

	#game caption
	ai_stngs.ai_caption("Alien Invasion")

	#instantiate the ship objec
	ai_ship = ship.Ship(ai_stngs, screen)

	# Make a group to store bullets in.
	bullets = Group()

	# Make a group to store aliens in.
	aliens = Group()

	# Create the fleet of aliens.
	GF.create_fleet(ai_stngs, screen, ai_ship, aliens)
	while True:

		GF.check_events(ai_stngs, screen, ai_ship, bullets)

		#ship movement
		ai_ship.update()

		 
		GF.update_bullets(bullets)

		GF.update_aliens(aliens)
		
		GF.update_screen(ai_stngs, screen, ai_ship, bullets, aliens)
		# Make the most recently drawn screen visible.
		pygame.display.flip()

run_game()
