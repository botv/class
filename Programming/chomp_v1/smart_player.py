import random

from constants import *


class SmartPlayer:
	@staticmethod
	def get_move(board):
		moves = board.get_possible_moves()
		new_boards = [board.get_new_board(move) for move in moves]
		best_move = None

		if len(moves) == 0:
			return ROWS - 1, 0

		for move in moves:
			new_board = board.get_new_board(move)




		return move
