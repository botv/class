import random

from constants import *


class Player:
	def __init__(self, epsilon):
		self.moves = []
		self.epsilon = epsilon

	@staticmethod
	def get_move(board):
		moves = board.get_possible_moves()
		if len(moves) == 0:
			return ROWS - 1, 0
		move = random.choice(moves)
		return move
