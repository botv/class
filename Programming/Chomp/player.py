import random

from constants import *


class Player:
	@staticmethod
	def move(board, row, column):
		new_board = list(board)

		if new_board[column] > (ROWS - 2 - row):
			new_board[column] = (ROWS - 1 - row)

			for c in range(column, COLUMNS):
				if new_board[c] > new_board[column]:
					new_board[c] = new_board[column]

		return new_board

	@staticmethod
	def get_moves(board):
		moves = []
		for column, rows in enumerate(board):
			for row in range(rows):
				move = (ROWS - 1 - row, column)
				if move != (ROWS - 1, 0):
					moves.append(move)
		return moves

	def get_reductions(self, board, reductions=None):
		if reductions is None:
			reductions = {}

		moves = self.get_moves(board)

		for index, move in enumerate(moves):
			row, column = move
			new_board = self.move(board, row, column)
			if str(board) not in reductions:
				reductions[str(board)] = [new_board]
			else:
				if new_board not in reductions[str(board)]:
					reductions[str(board)].append([new_board])
			self.get_reductions(new_board, reductions)
		return reductions

	def get_paths(self, board, paths=None, index=0):
		if paths is None:
			paths = []

		if len(paths) <= index:
			paths.append([])

		moves = self.get_moves(board)

		for move in moves:
			paths[index].append(board)
			row, column = move
			new_board = self.move(board, row, column)

			print(paths[index])
			if new_board in paths[index]:
				self.get_paths(new_board, paths, index+1)
			else:
				self.get_paths(new_board, paths, index)

		return paths

	def get_move(self, board):
		moves = self.get_moves(board)
		if len(moves) == 0:
			return ROWS - 1, 0
		move = random.choice(moves)
		return move
