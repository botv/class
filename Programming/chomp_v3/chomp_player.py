class ChompPlayer:
	def __init__(self, board_size=3):
		self.board_size = board_size
		self.winning_boards = list()
		self.losing_boards = list()

	def get_all_boards(self, n, size, depth=0):
		boards = list()
		if depth == size - 1:
			for i in range(n + 1):
				boards.append([i])
			return boards
		for i in range(n + 1):
			temp = self.get_all_boards(i, size, depth + 1)
			for j in temp:
				j.insert(0, i)
				boards.append(j)
		return boards[1::]

	def get_boards(self):
		boards = self.get_all_boards(self.board_size, self.board_size)
		for board in boards:
			self.think(board)

	def think(self, parent_board):
		for board in self.get_children(parent_board):
			if board in reversed(self.winning_boards):
				self.losing_boards.append(parent_board)
				return
		self.winning_boards.append(parent_board)

	def get_children(self, board):
		boards = list()
		for i in range(len(board)):
			for j in range(1, board[i] + 1):
				temp = list()
				temp = board.copy()
				for k in range(i, len(board)):
					if k == i:
						temp[k] -= j
					elif temp[k] > temp[k - 1]:
						temp[k] = temp[k - 1]
				boards.append(temp)
		return boards

	def get_path(self, board):
		boards = list()
		i_val = list()
		j_val = list()
		for i in range(len(board)):
			for j in range(1, board[i] + 1):
				temp = board.copy()
				for k in range(i, len(board)):
					if k == i:
						temp[k] -= j
					elif temp[k] > temp[k - 1]:
						temp[k] = temp[k - 1]
				boards.append(temp)
				i_val.append(i + 1)
				j_val.append(temp[i] + 1)
		return boards, i_val, j_val

	def get_move(self, board):
		boards, i_val, j_val = self.get_path(board)
		for i, b in enumerate(boards):
			if b in self.winning_boards:
				return i_val[i] - 1, j_val[i]
		return self.board_size - 1, 0
