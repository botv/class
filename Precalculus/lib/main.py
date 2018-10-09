import precalc

if __name__ == '__main__':
	DEPTH = 100
	triangle = precalc.PascalsTriangle(DEPTH)
	print(triangle)
	triangle.graph_max_values()

# SIZE = 10
# table = precalc.PascalsTriangleColumns(SIZE)
# print(table)
