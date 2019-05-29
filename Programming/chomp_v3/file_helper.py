import numpy as np
from os import path


class FileHelper:
	@staticmethod
	def save(filename, data):
		np.savetxt(filename, data)

	@staticmethod
	def load(filename):
		return np.loadtxt(filename).tolist()

	@staticmethod
	def exists(filename):
		return path.exists(filename)
