from progress.bar import Bar

from file_helper import FileHelper


class ChompPlayer:
	def __init__(self, board_size=3):
		self.board_size = board_size
		self.winning_boards = list()
		self.losing_boards = list()

	def get_all_boards(self, board_size, n, depth=0):
		boards = list()
		if depth == board_size - 1:
			for i in range(n + 1):
				boards.append([i])
			return boards
		for i in range(n + 1):
			temp = self.get_all_boards(board_size, i, depth + 1)
			for j in temp:
				j.insert(0, i)
				boards.append(j)
		return boards

	def load_boards(self):
		winning_boards_file = './boards/{}x{}_winning_boards.txt'.format(self.board_size, self.board_size)
		losing_boards_file = './boards/{}x{}_losing_boards.txt'.format(self.board_size, self.board_size)

		if FileHelper.exists(winning_boards_file) and FileHelper.exists(losing_boards_file):
			self.winning_boards = FileHelper.load(winning_boards_file)
			self.losing_boards = FileHelper.load(losing_boards_file)

		else:
			boards = self.get_all_boards(self.board_size, self.board_size)
			boards.remove([0 for _ in range(self.board_size)])
			bar = Bar('Loading boards', max=len(boards))
			for board in boards:
				self.think(board)
				bar.next()
			bar.finish()

			FileHelper.save(winning_boards_file, self.winning_boards)
			FileHelper.save(losing_boards_file, self.losing_boards)

	def think(self, parent_board):
		for board in self.get_children(parent_board):
			if board in reversed(self.losing_boards):
				self.winning_boards.append(parent_board)
				return
		self.losing_boards.append(parent_board)

	def get_children(self, board):
		boards = list()
		for i in range(len(board)):
			for j in range(1, board[i] + 1):
				new_board = board.copy()
				for k in range(i, len(board)):
					if k == i:
						new_board[k] -= j
					elif new_board[k] > new_board[k - 1]:
						new_board[k] = new_board[k - 1]
				boards.append(new_board)
		return boards

	def get_move(self, board):
		for move in board.get_possible_moves():
			new_board = board.get_new_board(move)
			if new_board.board in self.losing_boards:
				return move
		return board.get_possible_moves()[0]
