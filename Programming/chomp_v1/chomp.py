import random

from board import Board
from random_player import RandomPlayer


class Chomp:
	@staticmethod
	def play_game(rows, cols):
		board = Board(rows, cols)
		winner = None
		loser = None
		game_over = False
		p1 = RandomPlayer()
		p2 = RandomPlayer()
		turn = 0

		while not game_over:
			turn += 1

			if turn % 2 == 0:
				move = p1.get_move(board)
				board.update(move)

				if board.is_terminal():
					game_over = True
					winner = p2
					loser = p1

			elif turn % 2 == 1:
				move = p2.get_move(board)
				board.update(move)

				if board.is_terminal():
					game_over = True
					winner = p1
					loser = p2

		return winner.moves, loser.moves

	def train(self, num_games, rows, cols):
		state_values = {}

		for game in range(num_games):
			winner_moves, loser_moves = self.play_game(rows, cols)
			print(winner_moves, loser_moves)