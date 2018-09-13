import numpy as np


def generate_array():
	return np.random.randint(0, 9, size=[10, 10])


def find_path(arr):
	indeces = []
	x, y = 0


if __name__ == '__main__':
	arr = generate_array()
	print(arr)
