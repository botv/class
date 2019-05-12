import numpy as np
import pygame

from chomp_agent import ChompAgent
from chomp_board import ChompBoard
from constants import *
from file_helper import FileHelper


def optimize(board, winner, loser):
	winner.on_reward(board, 1)
	loser.on_reward(board, -1)


def train(epochs, agent1, agent2):
	agents = [{
		'mdl': agent1,
		'name': 'Agent 1',
		'wins': 0
	}, {
		'mdl': agent2,
		'name': 'Agent 2',
		'wins': 0
	}]

	for epoch in range(epochs):
		print('-' * 100)
		print('Epoch: {}'.format(epoch + 1))
		board = ChompBoard(size=5)
		game_over = False

		while not game_over:
			for agent in agents:
				move = agent['mdl'].select_move(board)
				board.update(move)
				if board.is_terminal():
					game_over = True
					loser = agent
					winner = agents[0] if agents[1] == agent else agents[1]
					print('Winner:', agent['name'])
					optimize(board, winner['mdl'], loser['mdl'])
					winner['wins'] += 1
					break


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


def human_play(agent):
	print('-' * 100)
	print('Human Play')
	board = ChompBoard(size=5)
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

							board.update((row, col))
							draw_board(screen, board)

							game_over = board.is_terminal()
							if game_over:
								print('Winner: Agent')
								break

							# Computer player move
							move = agent.select_move(board)
							board.update(move)
							draw_board(screen, board)

							game_over = board.is_terminal()
							if game_over:
								print('Winner: Human')
								break

					except IndexError:
						pass

	pygame.display.quit()
	pygame.quit()


def save_states(agent):
	data = {k: v.tolist() for k, v in agent.states.items()}
	FileHelper.save(data, 'data/states.json')


def load_states():
	data = FileHelper.load('data/states.json')
	return {k: np.array(v) for k, v in data.items()}


def main():
	# agent1 = ChompAgent()
	# agent2 = ChompAgent()
	# epochs = 10000
	# train(epochs, agent1, agent2)
	# save_states(agent2)

	agent = ChompAgent()
	agent.states = load_states()
	agent.get_serious()
	human_play(agent)


if __name__ == '__main__':
	main()
