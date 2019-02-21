"""
Chomp AI Player
Author: Lei Mao
Website: https://github.com/leimao
Date: 2017/3/23
Content: Play Chomp with AI in PyGame Gui.
Acknowledgement: http://programarcadegames.com
"""

import pygame
import numpy as np
import player

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
ORANGE = (255, 128, 0)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20
ROWS = 12
COLUMNS = 12
MARGIN = 2


def draw_board(board):
	for c in range(COLUMNS):
		for r in range(ROWS):
			color = WHITE

			if board[c] <= (ROWS - 1 -r):
				color = GRAY

			pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * c + MARGIN, (MARGIN + HEIGHT) * r + MARGIN, WIDTH, HEIGHT])

	color = ORANGE
	pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * 0 + MARGIN, (MARGIN + HEIGHT) * (ROWS - 1) + MARGIN, WIDTH, HEIGHT])

	pygame.display.flip()


if __name__ == '__main__':
	# Initialize board full of cookies
	board = np.full(COLUMNS, fill_value=ROWS, dtype=int)

	# Initialize pygame
	pygame.init()

	# Set the HEIGHT and WIDTH of the screen
	board_size_x = int((WIDTH + MARGIN) * COLUMNS + MARGIN)
	board_size_y = int((HEIGHT + MARGIN) * ROWS + MARGIN)

	window_size_x = int(board_size_x)
	window_size_y = int(board_size_y)

	screen = pygame.display.set_mode([window_size_x, window_size_y])

	# Set title of screen
	pygame.display.set_caption('Chomp')

	# Loop until the user clicks the close button.
	game_over = False

	# Used to manage how fast the screen updates
	clock = pygame.time.Clock()

	# Limit to 60 frames per second
	clock.tick(60)

	# Set the screen background
	screen.fill(BLACK)

	while not game_over:
		draw_board(board)
		user_clicked = False
		while not user_clicked:
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					pos = pygame.mouse.get_pos()
					column = pos[0] // (WIDTH + MARGIN)
					row = pos[1] // (HEIGHT + MARGIN)

					try:
						if board[column] > (ROWS - 2 - row):
							user_clicked = True
							board[column] = (ROWS - 1 - row)

							for c in range(column, COLUMNS):
								if board[c] > board[column]:
									board[c] = board[column]

							print(board)

						if row == ROWS - 1 and column == 0:
							game_over = True
					except IndexError:
						pass

	pygame.display.quit()

	# Be IDLE friendly. If you forget this line, the program will 'hang' on exit.
	pygame.quit()
