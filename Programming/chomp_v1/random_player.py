import random

from constants import *


class RandomPlayer:
	def __init__(self):
		self.moves = {}

	def get_move(self, board):
		moves = board.get_possible_moves()
		if len(moves) == 0:
			return board.rows - 1, 0
		move = random.choice(moves)
		self.moves[str(board)] = move
		return move
