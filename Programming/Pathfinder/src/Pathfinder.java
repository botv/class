import java.util.ArrayList;

class Pathfinder {
	private Grid grid;
	private int finalx;
	private int finaly;
	private double smallestScore = Double.MAX_VALUE;

	Pathfinder(Grid grid, int finalx, int finaly) {
		this.grid = grid;
		this.finalx = finalx;
		this.finaly = finaly;
	}

	private ArrayList<String> findShortestPaths(int x, int y, String pathSoFar, double scoreSoFar,
	                                        ArrayList<String> paths) {
		if (x == finalx && y == finaly) {
			smallestScore = scoreSoFar;
			System.out.println(pathSoFar + ": " + smallestScore);
			paths.add(pathSoFar);
		} else {
			if (x < finalx) {
				double scoreOfMove = grid.tiles[x + 1][y].resistance;
				if (scoreOfMove + scoreSoFar < smallestScore) {
					paths = findShortestPaths(x + 1, y, pathSoFar + "d", scoreSoFar + scoreOfMove, paths);
				}
			}

			if (y < finaly) {
				double scoreOfMove = grid.tiles[x][y + 1].resistance;
				if (scoreOfMove + scoreSoFar < smallestScore) {
					paths = findShortestPaths(x, y + 1, pathSoFar + "r", scoreSoFar + scoreOfMove, paths);
				}
			}

			if (x > finalx) {
				double scoreOfMove = grid.tiles[x - 1][y].resistance;
				if (scoreOfMove + scoreSoFar < smallestScore) {
					paths = findShortestPaths(x - 1, y, pathSoFar + "u", scoreSoFar + scoreOfMove, paths);
				}
			}

			if (y > finaly) {
				double scoreOfMove = grid.tiles[x][y - 1].resistance;
				if (scoreOfMove + scoreSoFar < smallestScore) {
					paths = findShortestPaths(x, y - 1, pathSoFar + "l", scoreSoFar + scoreOfMove, paths);
				}
			}
		}

		return paths;
	}

	String findShortestPath(int x, int y) {
		ArrayList<String> shortestPaths = findShortestPaths(x, y, "", 0, new ArrayList<>());
		System.out.println();
		return shortestPaths.get(shortestPaths.size() - 1);
	}

	ArrayList<String> findAllPaths(int x, int y, String pathSoFar, ArrayList<String> paths) {

		if (x == finalx && y == finaly) {
			paths.add(pathSoFar);
		} else {
			if (x < finalx) {
				double scoreOfMove = grid.tiles[x + 1][y].resistance;
				paths = findAllPaths(x + 1, y, pathSoFar + "d", paths);
			}

			if (y < finaly) {
				double scoreOfMove = grid.tiles[x][y + 1].resistance;
				paths = findAllPaths(x, y + 1, pathSoFar + "r", paths);
			}

			if (x > finalx) {
				double scoreOfMove = grid.tiles[x - 1][y].resistance;
				paths = findAllPaths(x - 1, y, pathSoFar + "u", paths);
			}

			if (y > finaly) {
				double scoreOfMove = grid.tiles[x][y - 1].resistance;
				paths = findAllPaths(x, y - 1, pathSoFar + "l", paths);
			}
		}

		return paths;
	}
}
