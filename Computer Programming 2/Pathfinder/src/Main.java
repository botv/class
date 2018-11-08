import java.awt.Canvas;
import java.awt.Dimension;
import java.awt.Graphics2D;
import java.awt.event.*;
import java.awt.image.BufferStrategy;

import javax.swing.JFrame;
import javax.swing.JPanel;
import java.awt.*;
import java.util.ArrayList;

public class Main implements Runnable, MouseListener {

	private final int WIDTH = 900;
	private final int HEIGHT = 700;

	private BufferStrategy bufferStrategy;
	private Image image;

	private boolean moving;

	private String path = "";
	private String direction = "";

	private int xpos = 400;
	private int ypos = 300;
	private int xdest = 400;
	private int ydest = 300;
	private Grid grid = new Grid(7, 9);

	public static void main(String[] args) {
		Main ex = new Main();
		new Thread(ex).start();
	}

	private Main() {
		JFrame frame = new JFrame("Pathfinder");

		JPanel panel = (JPanel) frame.getContentPane();
		panel.setPreferredSize(new Dimension(WIDTH, HEIGHT));
		panel.setLayout(null);

		Canvas canvas = new Canvas();
		canvas.setBounds(0, 0, WIDTH, HEIGHT);
		canvas.setIgnoreRepaint(true);

		panel.add(canvas);

		canvas.addMouseListener(this);

		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.pack();
		frame.setResizable(false);
		frame.setVisible(true);

		image = Toolkit.getDefaultToolkit().getImage(
				"images/sprite.jpg");

		canvas.createBufferStrategy(2);
		bufferStrategy = canvas.getBufferStrategy();

		canvas.requestFocus();
	}

	public void run() {

		while (true) {
			// paint the graphics
			render();

			if (path.length() > 0 && ypos % 100 == 0 && xpos % 100 == 0) {
				direction = path.substring(0, 1);
				path = path.substring(1);
			}

			if (xpos == xdest && ypos == ydest) {
				moving = false;
				direction = "";
			}

			switch (direction) {
				case "u":
					ypos -= 1;
					break;
				case "d":
					ypos += 1;
					break;
				case "l":
					xpos -= 1;
					break;
				case "r":
					xpos += 1;
					break;
			}

			//sleep
			try {
				Thread.sleep(5);
			} catch (InterruptedException ignored) {

			}
		}
	}

	private void render() {
		Graphics2D g = (Graphics2D) bufferStrategy.getDrawGraphics();
		g.clearRect(0, 0, WIDTH, HEIGHT);

		for (int x = 0; x < WIDTH / 100; x++) {
			for (int y = 0; y < HEIGHT / 100; y++) {
				g.setColor(grid.tiles[y][x].color);
				g.fillRect(x * 100, y * 100, 100, 100);
			}
		}

		g.drawImage(image, xpos, ypos, 100, 100, null);
		g.dispose();
		bufferStrategy.show();
	}

	public void mouseClicked(MouseEvent e) {
	}

	public void mousePressed(MouseEvent e) {
	}

	public void mouseEntered(MouseEvent e) {
	}

	public void mouseExited(MouseEvent e) {
	}

	public void mouseReleased(MouseEvent e) {
		if (!moving) {
			moving = true;
			xdest = (e.getX() / 100) * 100;
			ydest = (e.getY() / 100) * 100;
			Pathfinder pathfinder = new Pathfinder(grid, e.getY() / 100, e.getX() / 100);
			ArrayList<String> paths = pathfinder.findAllPaths(ypos / 100, xpos / 100, "", new ArrayList<>());
			path = pathfinder.findShortestPath(ypos / 100, xpos / 100);
		}
	}
}