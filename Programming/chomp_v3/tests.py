import time


class Player():
	def __init__(self, size):
		self.size = size
		self.win = list()
		self.lose = list()

	def pos(self, n, size, depth=0):
		boards = list()
		if depth == size - 1:
			for i in range(n + 1):
				boards.append([i])
			return boards
		for i in range(n + 1):
			temp = self.pos(i, size, depth + 1)
			for j in temp:
				j.insert(0, i)
				boards.append(j)
		return boards

	def boards(self, size):
		boards = self.pos(size, size)
		boards.pop(0)
		return boards

	def get_boards(self):
		bs = self.boards(self.size)
		print(bs)
		print("GOTTEN " + str(len(bs)) + " BOARDS")
		n = 0
		for b in bs:
			# print(b)
			n += 1
			print(str(round(100 * n / len(bs), 2)) + "%", end="\r")
			self.think(b)

	def think(self, parent_board):
		for b in self.get_children(parent_board):
			if b in reversed(self.win):
				self.lose.append(parent_board)
				return
		self.win.append(parent_board)

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
		boards, i_vals, j_vals = self.get_path(board)
		for i, b in enumerate(boards):
			if b in self.win:
				return i_vals[i], j_vals[i]


def main():
	player = Player(2)
	player.get_boards()
	print(player.win)
	print(player.lose)

	while True:
		inp = list()
		for n in range(player.size):
			inp.append(int(input("Input number " + str(n + 1) + ": ")))
		print(inp)
		print(player.get_move(inp))


if __name__ == '__main__':
	main()
