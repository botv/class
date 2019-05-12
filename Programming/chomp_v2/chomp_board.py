import numpy as np


class ChompBoard:
	def __init__(self, size=3):
		self.size = size
		self.board = np.full(size, fill_value=size, dtype=int)
		self.losing_board = '0' * size
		self.winner = None
		self.loser = None

	def reset(self):
		self.board = np.full(self.size, fill_value=self.size, dtype=int)
		self.winner = None
		self.loser = None

	def serialize(self):
		return ''.join(map(str, self.board))

	def is_terminal(self):
		if self.serialize() == self.losing_board:
			return True
		else:
			return False

	def update(self, move):
		new_board = self.get_new_board(move)
		self.board = new_board

	def get_new_board(self, move):
		row, column = move
		new_board = list(self.board)

		if new_board[column] > (self.size - 2 - row):
			new_board[column] = (self.size - 1 - row)

			for c in range(column, self.size):
				if new_board[c] > new_board[column]:
					new_board[c] = new_board[column]

		return new_board

	def get_possible_moves(self):
		moves = []

		for column, rows in enumerate(self.board):

			for row in range(rows):
				move = (self.size - 1 - row, column)

				moves.append(move)

		return moves
