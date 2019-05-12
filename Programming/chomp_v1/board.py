import numpy as np

from constants import *


class Board:
	def __init__(self, rows, cols):
		self.rows = rows
		self.cols = cols
		self.board = np.full(cols, fill_value=rows, dtype=int)
		self.losing_board = self.get_losing_board(cols)

	def __str__(self):
		return ''.join(map(str, self.board))

	def update(self, move):
		new_board = self.get_new_board(move)
		self.board = new_board

	def get_new_board(self, move):
		row, column = move
		new_board = list(self.board)

		if new_board[column] > (self.rows - 2 - row):
			new_board[column] = (self.rows - 1 - row)

			for c in range(column, self.cols):
				if new_board[c] > new_board[column]:
					new_board[c] = new_board[column]

		return new_board

	def get_possible_new_boards(self):
		moves = self.get_possible_moves()
		return [self.get_new_board(move) for move in moves]

	def get_possible_moves(self):
		moves = []

		for column, rows in enumerate(self.board):

			for row in range(rows):
				move = (self.rows - 1 - row, column)

				if move != (self.rows - 1, 0):
					moves.append(move)

		return moves

	def get_reductions(self):
		moves = self.get_possible_moves()
		reductions = []

		for move in moves:
			reductions.append(self.update(move))

		return reductions

	def get_losing_board(self, columns):
		losing_board = np.full(columns, fill_value=0, dtype=int)
		losing_board[0] = 1
		return losing_board

	def is_terminal(self):
		if np.array_equal(self.board, self.losing_board):
			return True
		else:
			return False
