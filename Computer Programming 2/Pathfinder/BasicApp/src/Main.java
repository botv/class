import java.awt.Canvas;
import java.awt.Dimension;
import java.awt.Graphics2D;
import java.awt.event.*;
import java.awt.image.BufferStrategy;

import javax.swing.JFrame;
import javax.swing.JPanel;
import java.awt.*;

public class Main implements Runnable, KeyListener, MouseListener {

	private final int WIDTH = 900;
	private final int HEIGHT = 700;

	private BufferStrategy bufferStrategy;
	private Image image;

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

		canvas.addKeyListener(this);
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

			// move things
			if (xpos != xdest && ypos % 100 == 0) {
				xpos += Math.abs(xdest - xpos) / (xdest - xpos);
			} else if (ypos != ydest && xpos % 100 == 0) {
				ypos += Math.abs(ydest - ypos) / (ydest - ypos);
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

	public void keyPressed(KeyEvent e) {

	}

	public void keyReleased(KeyEvent e) {

	}

	public void keyTyped(KeyEvent e) {
		System.out.println("Key Typed: " + e.getKeyChar() + " "
				+ InputEvent.getModifiersExText(e.getModifiersEx()) + "\n");
	}

	@Override
	public void mouseClicked(MouseEvent e) {

	}

	@Override
	public void mousePressed(MouseEvent e) {

	}

	@Override
	public void mouseReleased(MouseEvent e) {
		xdest = ((int) e.getX() / 100) * 100;
		ydest = ((int) e.getY() / 100) * 100;
		System.out.println("(" + xdest + ", " + ydest + ")");
	}

	@Override
	public void mouseEntered(MouseEvent e) {

	}

	@Override
	public void mouseExited(MouseEvent e) {

	}
}