import pygame

from chomp_player import ChompPlayer
from chomp_board import ChompBoard
from constants import *


def draw_board(screen, board):
	for c in range(board.size):
		for r in range(board.size):
			color = WHITE

			if board.board[c] <= (board.size - 1 - r):
				color = GRAY

			pygame.draw.rect(screen, color,
				[(MARGIN + WIDTH) * c + MARGIN, (MARGIN + HEIGHT) * r + MARGIN, WIDTH, HEIGHT])

	color = ORANGE
	pygame.draw.rect(screen, color,
		[(MARGIN + WIDTH) * 0 + MARGIN, (MARGIN + HEIGHT) * (board.size - 1) + MARGIN, WIDTH, HEIGHT])

	pygame.display.flip()


def play(player, board_size=3):
	board = ChompBoard(size=board_size)
	pygame.init()

	# Set the HEIGHT and WIDTH of the screen
	board_size_x = int((WIDTH + MARGIN) * board.size + MARGIN)
	board_size_y = int((HEIGHT + MARGIN) * board.size + MARGIN)

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

	# Draw the screen
	draw_board(screen, board)

	while not game_over:
		user_clicked = False
		while not user_clicked:
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					# Human player move
					pos = pygame.mouse.get_pos()
					col = pos[0] // (WIDTH + MARGIN)
					row = pos[1] // (HEIGHT + MARGIN)

					try:
						if board.board[col] > (board.size - 2 - row):
							user_clicked = True

							# Player move
							move = (row, col)
							board.update(move)
							draw_board(screen, board)

							game_over = board.is_terminal()
							if game_over:
								print('Winner: computer')
								break

							# Computer move
							move = player.get_move(board.board)
							print(move)
							board.update(move)
							draw_board(screen, board)

							game_over = board.is_terminal()
							if game_over:
								print('Winner: player')
								break

					except IndexError:
						pass

	pygame.display.quit()
	pygame.quit()


def main():
	board_size = 2

	player = ChompPlayer(board_size=board_size)
	player.get_boards()

	play(player, board_size=board_size)


if __name__ == '__main__':
	main()
