from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd


if __name__ == '__main__':
	fig = plt.figure()

	ax = fig.add_subplot(111, projection='3d')
	df = pd.read_csv('../data/data.csv')

	x = df.iloc[:, 0]
	y = df.iloc[:, 1]
	z1 = df.iloc[:, 2]
	z2 = df.iloc[:, 3]
	z3 = df.iloc[:, 4]

	ax.scatter(x, y, z1)
	ax.scatter(x, y, z2)
	ax.scatter(x, y, z3)

	ax.set_xlabel('$NaOH$ (mL)')
	ax.set_ylabel('$CaCl_2$ (mL)')
	ax.set_zlabel('pH')

	plt.show()
