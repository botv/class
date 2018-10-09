import numpy as np


class Gridworld:
	def __init__(self, width=3, height=3):
		self.grid = np.random.rand(width, height)

	def __str__(self):
		return str(self.grid)