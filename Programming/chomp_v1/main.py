"""
Chomp AI Player
Author: Lei Mao
Website: https://github.com/leimao
Date: 2017/3/23
Content: Play Chomp with AI in PyGame Gui.
Acknowledgement: http://programarcadegames.com
"""

import pygame

from chomp import Chomp
from smart_player import *
from board import *


def draw_board(board):
	for c in range(COLUMNS):
		for r in range(ROWS):
			color = WHITE

			if board[c] <= (ROWS - 1 - r):
				color = GRAY

			pygame.draw.rect(screen, color,
				[(MARGIN + WIDTH) * c + MARGIN, (MARGIN + HEIGHT) * r + MARGIN, WIDTH, HEIGHT])

	color = ORANGE
	pygame.draw.rect(screen, color,
		[(MARGIN + WIDTH) * 0 + MARGIN, (MARGIN + HEIGHT) * (ROWS - 1) + MARGIN, WIDTH, HEIGHT])

	pygame.display.flip()


def main():
	# Initialize board full of cookies
	board = Board(ROWS, COLUMNS)

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
		player = SmartPlayer()
		print(board.board)

		draw_board(board.board)
		user_clicked = False
		while not user_clicked:
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					# Human player move
					pos = pygame.mouse.get_pos()
					column = pos[0] // (WIDTH + MARGIN)
					row = pos[1] // (HEIGHT + MARGIN)

					try:
						if board.board[column] > (ROWS - 2 - row):
							user_clicked = True
							board.board[column] = (ROWS - 1 - row)

							for c in range(column, COLUMNS):
								if board.board[c] > board.board[column]:
									board.board[c] = board.board[column]

							if row == ROWS - 1 and column == 0:
								game_over = True

							# Computer player move
							move = player.get_move(board)
							board.update(move)

							if row == ROWS - 1 and column == 0:
								game_over = True

					except IndexError:
						pass

	pygame.display.quit()
	pygame.quit()


if __name__ == '__main__':
	chomp = Chomp()
	chomp.train(100, 3, 3)
