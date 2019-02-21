public class MyPlayerApp extends Player {
	public int[] column = new int[10];
	public int[] row = new int[10];
	public Chip[] gameBoard = new Chip[100];
	public int counter;

	public int move(Chip[] chip) {

		gameBoard = chip;
		countCols();
		countRows();
		System.out.println("");

		if (gameBoard[18].isAlive && column[0] == row[9]) {
			return (18);
		}

		return (9);
	}


	public void countCols() {
		System.out.print("Column counter:");
		for (int i = 0; i < 10; i++) {
			for (int a = 0; a < 10; a++) {
				if (gameBoard[i * 10 + a].isAlive) {
					counter++;
				}
			}
			column[i] = counter;
			System.out.print("" + column[i] + " ");
			counter = 0;
		}
		System.out.println("");
	}

	public void countRows() {
		System.out.print("Row counter:");
		for (int i = 0; i < 10; i++) {
			for (int a = 0; a < 10; a++) {
				if (gameBoard[i + 10 * a].isAlive) {
					counter++;
				}
			}
			row[i] = counter;
			System.out.print("" + row[i] + " ");
			counter = 0;
		}
		System.out.println("");
	}


}

