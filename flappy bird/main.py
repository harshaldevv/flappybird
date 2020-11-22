import pygame
import random
import sys
from pygame.locals import*

FPS = 32
SCREENWIDTH = 289		
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
GROUNDY = SCREENHEIGHT*0.8
clock_tick_rate = 20
clock = pygame.time.Clock()


GAME_SPIRTES = {}
GAME_SOUNDS = {}

background = "gallery2/gallery_new/background.png"
#background = pygame.image.load("gallery/background.png").convert()
player =  "gallery2/gallery_new/bird.png"
#player =  pygame.image.load("gallery/bird.jpg").convert_alpha()
pipe =  "gallery2/gallery_new/pipe.png"
#pipe =  pygame.image.load("gallery/pipe.png").convert_alpha()
pipe2 = "gallery2/gallery_new/pipe2.png"
#pipe2 = pygame.image.load("gallery/pipe2.png").convert_alpha()

#def welcomeScreen():
#	playerx = int(SCREENWIDTH/5)
#	playery = int(SCREENHEIGHT - GAME_SPIRTES)
def welcomeScreen():
	"""shows welcome screen"""
	playerx = int(SCREENWIDTH/5)
	playery = int((SCREENHEIGHT - GAME_SPIRTES['player'].get_height())/2)

	messagex = int((SCREENHEIGHT - GAME_SPIRTES['message'].get_width())/2)
	messagey = int(SCREENHEIGHT*0.13)

	basex = 0

	while True:
		for event in pygame.event.get():

			if event.type == pygame.QUIT or ( event.type == KEYDOWN and event.type == K_ESCAPE):
				pygame.quit()
				sys.exit()

			elif event.type == KEYDOWN and ( event.type == K_SPACE or event.key == K_UP):
				return 
		# wapis chale jao and will then play maingame func
			else:
				SCREEN.blit(GAME_SPIRTES['background'],(0,0))
				SCREEN.blit(GAME_SPIRTES['player'],(playerx,playery))
#				SCREEN.blit(GAME_SPIRTES['message'],(messagex,messagey))
				SCREEN.blit(GAME_SPIRTES['base'],(basex,GROUNDY))
				pygame.display.update()
				FPSCLOCK.tick(FPS)

def mainGame():
	score = 0
	playerx = int(SCREENWIDTH/5)
	playery = int(SCREENWIDTH/2)
	basex = 0

	#creating 2 pipes 

	newPipe1 = getRandomPipe()
	newPipe2 = getRandomPipe()

	#my list of upper pipes
	upperPipes = [
	{'x': SCREENWIDTH+200 , 'y':newPipe1[0]['y']},
	{'x':SCREENWIDTH+200+(SCREENWIDTH/2)  , 'y':newPipe2[0]['y']},



	]

	#my list of lower pipes.
	lowerPipes = [
	{'x': SCREENWIDTH+200 , 'y':newPipe1[1]['y']},
	{'x':SCREENWIDTH+200+(SCREENWIDTH/2)  , 'y':newPipe2[1]['y']},


	
	]

	pipeVelX = -4 

	playerVelY = -9

	playerMaxVelY= 10

	playerMinVelY = -8

	playerAccY = 1

	playerFlapAccv = -8 #velocity while flapping 

	playerFlapped = False #it is true only when the bird is flapping.

	while True:
		for event in pygame.event.get():
			if event.type == QUIT or (event.type==KEYDOWN and event.key == K_ESCAPE):
				pygame.quit()
				sys.exit()

			if event.type == KEYDOWN and (event.type == K_SPACE or event.key == K_UP):
				if playery >0:
					playerVelY = playerAccY
					playerFlapped = True
					GAME_SOUNDS['wing.'].play()



		
		crashTest = isCollide(playerx,playery,upperPipes,lowerPipes) #this func will return true if the player crashes
		

		if crashTest:
			return

		#check for score 

		playerMidPos = playerx+GAME_SPIRTES['player'].get_width()/2

		for pipe in upperPipes:
			pipeMidPos = pipe['x'] + GAME_SPIRTES['pipe'][0].get_width()/2
			if pipeMidPos <= playerMidPos < pipeMidPos +4:
				score +=1
				print(f"your score is{score}")


			GAME_SOUNDS['point'].play()


		if playerVelY < playerMaxVelY and not playerFlapped:
			playerVelY+= playerAccY


		if playerFlapped:
			playerFlapped = False

		playerHeight = GAME_SPIRTES['player'].get_height()
		playery = playery+min(playerVelY,GROUNDY - playery - playerHeight)

		#move pipes to the left

		for upperPipe , lowerPipe in zip(upperPipes,lowerPipes):
			upperPipe['x'] += pipeVelX
			lowerPipe['x'] += pipeVelX

		# add a new pipe when the first is about to cross the leftmost part of the screen.

		if 0<upperPipes[0]['x'] < 5:
			newpipe = getRandomPipe()
			upperPipes.append(newpipe[0])
			lowerPipes.append(newpipe[1])

		#if the piep is out of the screen, remove it.

		if upperPipes[0]['x'] < -GAME_SPIRTES['pipe'][0].get_width():
			upperPipes.pop(0)
			lowerPipes.pop(0)


		#let blit our sprites now

		SCREEN.blit(GAME_SPIRTES['background'],(0,0))
		for upperPipe , lowerPipe in zip(upperPipes,lowerPipes):

			SCREEN.blit(GAME_SPIRTES['pipe'][0],(upperPipe['x'],lowerPipe['y']))

			SCREEN.blit(GAME_SPIRTES['pipe'][1],(lowerPipe['x'],lowerPipe['y']))
			

		SCREEN.blit(GAME_SPIRTES['base'],(basex,GROUNDY))
		SCREEN.blit(GAME_SPIRTES['player'],(playerx,playery))


	myDigits = [int(x) for x in list(str(score))]
	width = 0

	for digit in myDigits:
		width += GAME_SPIRTES['numbers'][digit].get_width()


	Xoffset = (SCREENWIDTH - width)/2

	for digit in myDigits:
		SCREEN.blit(GAME_SPIRTES['numbers'][digit],(Xoffset,SCREENHEIGHT*0.12))
		Xoffset+= GAME_SPIRTES['numbers']['digit'].get_width()

	pygame.display.update()
	FPSCLOCK.tick(FPS)

		







	





def isCollide(playerx,playery,upperPipes,lowerPipes):
	if playery > GROUNDY-25 or playery <0:
		GAME_SOUNDS['hit'].play()
		return True



	for pipe in upperPipes:
		pipeHeight = GAME_SPIRTES['pipe'][0].get_height()
		pass

	for pipe in lowerPipes:
		pass
	return False




def getRandomPipe():
	"""generates 2 posn for two pipes ; ek seedha ek ulta """


	pipeHeight = GAME_SPIRTES['pipe'][0].get_height()
	y2 = offset + random.randrange(0, int(SCREENHEIGHT-GAME_SPIRTES['base'].get_height()) - 1.2*offset)
	y1 = pipeHeight - y2 +offset
	pipe = [
	{'x':pipeX,'y':-y1},
	{'x':pipeX,'y':y2}

	]
	return pipe




if __name__ == "__main__":
	pygame.init()
	FPSCLOCK = pygame.time.Clock()
	pygame.display.set_caption("Flappy bird by dholchike")
	GAME_SPIRTES['numbers'] = (
		pygame.image.load("gallery2/gallery_new/0.png").convert_alpha,
		pygame.image.load("gallery2/gallery_new/1.png").convert_alpha,
		pygame.image.load("gallery2/gallery_new/2.png").convert_alpha,
		pygame.image.load("gallery2/gallery_new/3.png").convert_alpha,
		pygame.image.load("gallery2/gallery_new/4.png").convert_alpha,
		pygame.image.load("gallery2/gallery_new/5.png").convert_alpha,
		pygame.image.load("gallery2/gallery_new/6.png").convert_alpha,
		pygame.image.load("gallery2/gallery_new/7.png").convert_alpha,
		pygame.image.load("gallery2/gallery_new/8.png").convert_alpha,
		pygame.image.load("gallery2/gallery_new/9.png").convert_alpha)

	GAME_SPIRTES["message"] = pygame.image.load("gallery2/gallery_new/message.png").convert_alpha()

	GAME_SPIRTES["base"] = pygame.image.load("gallery2/gallery_new/background.png").convert_alpha()

	GAME_SPIRTES["pipe"] =(pipe,pipe2) #(pygame.image.load(pipe).convert_alpha(),pygame.image.load(pipe2).convert_alpha())

	#game sounds

	GAME_SOUNDS["die"] = pygame.mixer.Sound("sounds/die.wav")
	GAME_SOUNDS["hit"] = pygame.mixer.Sound("sounds/hit.wav")
	GAME_SOUNDS["point"] = pygame.mixer.Sound("sounds/point.wav")
	GAME_SOUNDS["swoosh"] = pygame.mixer. Sound("sounds/swoosh.wav")
	GAME_SOUNDS["wing"] = pygame.mixer.Sound("sounds/wing.wav")

	GAME_SPIRTES["background"] = pygame.image.load(background).convert()
	GAME_SPIRTES["player"] = pygame.image.load(player).convert_alpha()








while True:

	welcomeScreen()
	mainGame()
	#shows welcome screen to the user

#	for event in pygame.event.get():
#		if event.type == pygame.QUIT:
#			pygame.exit()
#			sys.exit()

#	SCREEN.blit(background,[0,0])

#	pygame.display.flip()
#	clock.tick(clock_tick_rate)


