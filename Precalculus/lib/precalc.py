import matplotlib.pyplot as plt


class PascalsTriangle:
	def __init__(self, rows):
		# generate Pascal's Triangle up to the specified number of rows
		self.triangle = [[1], [1, 1]]
		for i in range(2, rows):
			row = [1]
			previous = self.triangle[i - 1]
			j = 1
			while j < len(previous):
				new = previous[j] + previous[j - 1]
				row.append(new)
				j += 1
			row.append(1)
			self.triangle.append(row)

	def __str__(self):
		# pretty string
		string = ''
		for row in self.triangle:
			string += (str(row) + '\n')
		return string.rstrip()

	def graph_max_values(self):
		# graph maximum values in rows of Pascal's Triangle
		plt.plot(range(1, len(self.triangle) + 1), list(max(row) for row in self.triangle), 'ro')
		plt.axis([1, len(self.triangle), 0, max(self.triangle[-1])])
		plt.xlabel('Row')
		plt.ylabel('Max Value')
		plt.title('Max Values of Rows in Pascal\'s Triangle')
		plt.grid(True)
		plt.show()


class PascalsTriangleColumns:
	def __init__(self, size):
		# generate the sequences that represent the columns of Pascal's Triangle
		self.table = [[1 for i in range(0, size)]]
		for i in range(1, size):
			row = []
			for j in range(0, size):
				row.append(sum(self.table[-1][0:j + 1]))
			self.table.append(row)

	def __str__(self):
		# pretty string
		string = ''
		for row in self.table:
			string += (str(row) + '\n')
		return string.rstrip()


class FibonacciSequence:
	def __init__(self, length):
		# generate the fibonacci sequence up to the specified length
		self.sequence = [1, 1]
		for i in range(2, length):
			self.sequence.append(self.sequence[-1] + self.sequence[-2])

	def get_value(self, n):
		# get a_n in the series
		return self.sequence[n]


class GeometricSequence:
	def __init__(self, terms, a, r):
		self.sequence = []
		for i in range(0, terms):
			self.sequence.append(a * (r ** i))

	def get_sum(self):
		sum = 0
		for term in self.sequence:
			sum += term
			print(sum)
		return sum