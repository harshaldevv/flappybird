import pygame
import sys


screenwidth = 1000
screenheight = 1000
screen = pygame.display.set_mode((screenwidth,screenheight))
clock_tick_rate = 20
clock = pygame.time.Clock()

background = pygame.image.load("gallery/bird.jpg").convert()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.exit()
			sys.exit()

	screen.blit(background,[0,0,])
	
	pygame.display.flip()
	clock.tick(clock_tick_rate)		





	##### main




import pygame
import random # for generating random numbers
import sys # we will use sys.exit to exit the program
from pygame.locals import * 

fps = 32
SCREENwidth = 289
SCREENheight = 511
SCREEN = pygame.display.set_mode((SCREENwidth,SCREENheight))
groundy = SCREENheight*0.8
game_sprites = {}
game_sounds = {}
player = "gallery/bird.jpg"
background = "gallery/background.png"
pipe = "gallery/pipe.png"
pipe2 = "gallery/pipe2.png"

def welcomeSCREEN():
	#shows the welcome image SCREEN 
	playerx = int(SCREENwidth/5)
	playery = int((SCREENheight- game_sprites["player"].get_height())/2)

	messagex = int((SCREENheight- game_sprites["message"].get_height())/2)
	maessagey = int(SCREENheight*0.13)

	basex = 0

	while True:
		for event in pygame.event.get():
			#if user clicks on "x" button , then the game will end
			if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
				pygame.quit()
				sys.exit()

				#IF the user presses space or up key , start the game 

			elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
				return

			else:
				SCREEN.blit(game_sprites["background"],(0,0))
				SCREEN.blit(game_sprites["player"],(playerx,playery))
				SCREEN.blit(game_sprites["message"],(messagex,maessagey))
				SCREEN.blit(game_sprites["base"],(basex,groundy))
				fpsclock.tick(fps)




	


if __name__ == "__main__":
	#this will be the main point from where our game will start

	pygame.init() # will initialse all pyagme modules
	fpsclock = pygame.time.Clock()
	pygame.display.set_caption("Flappy Bird by Dholchike Games")

	game_sprites["numbers"] = (
		pygame.image.load("C:/Users/harsh/Desktop/flappy bird/gallery/0.jpg").convert_alpha(),
		pygame.image.load("C:/Users/harsh/Desktop/flappy bird/gallery/1.jpg").convert_alpha(),
		pygame.image.load("C:/Users/harsh/Desktop/flappy bird/gallery/2.jpg").convert_alpha(),
		pygame.image.load("C:/Users/harsh/Desktop/flappy bird/gallery/3.jpg").convert_alpha(),
		pygame.image.load("C:/Users/harsh/Desktop/flappy bird/gallery/4.jpg").convert_alpha(),
		pygame.image.load("C:/Users/harsh/Desktop/flappy bird/gallery/5.jpg").convert_alpha(),
		pygame.image.load("C:/Users/harsh/Desktop/flappy bird/gallery/0.jpg").convert_alpha()
	

		)

	game_sprites["message"] = pygame.image.load("C:/Users/harsh/Desktop/flappy bird/gallery/0.jpg").convert_alpha()
	
	game_sprites["base"] = pygame.image.load("C:/Users/harsh/Desktop/flappy bird/gallery/0.jpg").convert_alpha()

	game_sprites["pipe"] = pygame.image.load(pipe),pygame.image.load(pipe2)
		#pygame.transform.rotate(pygame.image.load(pipe).convert_alpha(),180))

	#sounds
	game_sounds["die"] = pygame.mixer.music.load("C:/Users/harsh/Desktop/flappy bird/sounds/die.mp3")
	#i changed the "sound" to "music.load" . incase the sound doesnt work , just change the
	# audio to wav and replace music.load to "sound" . period. % MIC DROP%






	game_sprites["background"] = pygame.image.load(background).convert()
	game_sprites["player"] = pygame.image.load(player).convert_alpha()

	running = True

	while running:
		welcomeSCREEN()
		mainGame()










