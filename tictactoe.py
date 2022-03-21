#import modules
import pygame
from pygame.locals import *


pygame.init()

#game window
screen_height = 300
screen_width = 300
line_width = 6
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('TicTacToe')

#define colors
green = (0, 255, 0)
red = (50, 50, 50)
blue = (0, 0 , 255)

#define font
font = pygame.font.SysFont(None, 40)

#defining variables

markers = []
clicked = False
pos = (0,0)
player = 1
winner = 0
game_over = False

#create play again rectangle
again_rect = Rect(screen_width // 2 - 80, screen_height // 2, 160, 50)

#create empty 3x3 list for the grid
for x in range(3):
	row = [0] * 3
	markers.append(row)

#illustrating the gameboard
def draw_grid():
	bg = (255, 255, 200)
	grid = (50, 50, 50)
	screen.fill(bg)
	for x in range(1,3):
			pygame.draw.line(screen, grid, (0, 100 * x), (screen_width, 100 * x), line_width)
			pygame.draw.line(screen, grid, (100 * x, 0), (100 * x, screen_height), line_width)

def draw_markers():
	x_pos = 0
	for x in markers:
		y_pos = 0
		for y in x:
			if y == 1:
				pygame.draw.line(screen, red, (x_pos * 100 + 15, y_pos * 100 + 15), (x_pos * 100 + 85, y_pos * 100 + 85), line_width)
				pygame.draw.line(screen, red, (x_pos * 100 + 85, y_pos * 100 + 15), (x_pos * 100 + 15, y_pos * 100 + 85), line_width)
			if y == -1:
				pygame.draw.circle(screen, green, (x_pos * 100 + 50, y_pos * 100 + 50), 38, line_width)
			y_pos += 1
		x_pos += 1	


def check_winner():
	global game_over
	global winner

	x_pos = 0
	for x in markers:
		#check columns
		if sum(x) == 3:
			winner = 1
			game_over = True
		if sum(x) == -3:
			winner = 2
			game_over = True
		#check rows
		if markers[0][x_pos] + markers [1][x_pos] + markers [2][x_pos] == 3:
			winner = 1
			game_over = True
		if markers[0][x_pos] + markers [1][x_pos] + markers [2][x_pos] == -3:
			winner = 2
			game_over = True
		x_pos += 1

	#check cross
	if markers[0][0] + markers[1][1] + markers[2][2] == 3 or markers[2][0] == markers[1][1] + markers[0][2] == 3:
		winner = 1
		game_over = True
	if markers[0][0] + markers[1][1] + markers[2][2] == -3 or markers[2][0] == markers[1][1] + markers[0][2] == -3:
		winner = 2
		game_over = True

def draw_winner():
	win_text = 'Player' + str(winner) + 'Wins'
	win_img = font.render(win_text, True, blue)
	pygame.draw.rect(screen, green, (screen_width// 2 - 100, screen_height // 2 - 60, 200, 50))
	screen.blit(win_img, (screen_width // 2 - 100, screen_height // 2 - 50))

	again_text = 'Play Again?'
	again_img = font.render(again_text, True, blue)
	pygame.draw.rect(screen, green, again_rect)
	screen.blit(again_img(screen_width //2 - 80, screen_height // 2 + 10))


#creating the game loop, constantly looking for user interaction etc
run = True
while run:
	draw_grid()
	draw_markers()
		#add event handlers
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
				clicked = True
			if event.type == pygame.MOUSEBUTTONUP and clicked == True:
				clicked = False
				pos = pygame.mouse.get_pos()
				cell_x = pos[0]
				cell_y = pos[1]
				if markers[cell_x // 100][cell_y // 100] == 0:
					markers[cell_x // 100][cell_y // 100] = player
					player *= -1
					check_winner()

	if game_over == True:
		draw_winner(winner)
		#check for mouse click to see if user has clicked on play again
		if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
			clicked = True
		if event.type == pygame.MOUSEBUTTONUP and clicked == True:
			clicked = False
			pos = pygame.mouse.get_pos()
			if again_rect.collidepoint(pos):
					#reset variables
					markers = []
					pos = []
					player = 1
					winner = 0
					game_over = False
					for x in range(3):
						row = [0] * 3
						markers.append(row)
			



	pygame.display.update()

pygame.quit()

