import java.applet.*;
import java.awt.*;
import java.awt.event.*;
import java.util.*;
import java.net.*;
import java.io.*;

public class Chomp extends Frame implements ActionListener {

	public Rectangle mouserec;
	public int CELL_WIDTH = 25;
	public int NUM_ROWS = 10;
	public int NUM_COLLOMS = 10;
	public boolean position = false;
	public int xpos = 0, ypos = 0;
	public Chip[] piec = new Chip[101];
	public int chipNum = 0;
	public boolean youLose = false;
	public boolean legal = false;
	public Button start, suiside, random, notsmart, play;
	public Panel p = new Panel();

	public Player MrHales;
	public Player MrV;
	public NotSmartPlayer elmo;
	public SmartPlayer DrHales;

	public Player regPlayer;
	public RandomPlayer randomDude;
	public NotSmartPlayer dumbPlayer;
	public SmartPlayer smartDude;
	public MyPlayerApp myChomp;

	public String loser;

	public static void main(String[] args) {
		Chomp c = new Chomp();
		c.resize(400, 400);
		c.show();
	}

	public Chomp() {
		init();
	}

	public void init() {
		try {
			URL desktopURL = new URL("C:\\windows\\desktop\\");
		} catch (Exception e) {

		}

		smartDude = new SmartPlayer();
		dumbPlayer = new NotSmartPlayer();
		randomDude = new RandomPlayer();
		regPlayer = new Player();
		myChomp = new MyPlayerApp();

		start = new Button("NewGame");
		start.addActionListener(this);
		p.add(start);

		play = new Button("Play");
		play.addActionListener(this);
		p.add(play);

		random = new Button("random");
		random.addActionListener(this);
		p.add(random);

		notsmart = new Button("notsmart");
		notsmart.addActionListener(this);
		p.add(notsmart);

		suiside = new Button("MyChomp");
		suiside.addActionListener(this);
		p.add(suiside);

		setLayout(new BorderLayout());
		add("South", p);
		for (int i = 0; i < NUM_COLLOMS; i++) {

			for (int z = 0; z < NUM_ROWS; z++) {
				xpos = i * 25;
				ypos = z * 25 + 20;
				piec[chipNum] = new Chip(xpos + 18, ypos + 18, chipNum);
				if (chipNum < 100) {
					chipNum++;
				}
			}
		}
	}

	public boolean mouseDown(Event evt, int x, int y) {
		mouserec = new Rectangle(x, y, 2, 2);
		for (int z = 0; z < 100; z++) {

			if (mouserec.intersects(piec[z].myRect)) {

				move(z);
				repaint();
			}
		}
		return (true);
	}

	public void actionPerformed(ActionEvent e) {

		if (e.getActionCommand().equals("Play")) {
			System.out.println("play");
			while (youLose == false) {
				int num;
				loser = "player1";
				num = DrHales.move(piec);
				move(num);

				if (youLose == false) {
					loser = "player2";
					num = DrHales.move(piec);
					move(num);
				}
			}
		}
		if (e.getActionCommand().equals("NewGame")) {
			youLose = false;
			for (int z = 0; z < 100; z++) {
				piec[z].isAlive = true;
			}
			repaint();
		}

		if (e.getActionCommand().equals("MyChomp")) {
			int num;
			num = myChomp.move(piec);
			move(num);
			repaint();
		}

		if (e.getActionCommand().equals("notsmart")) {
			int num;
			num = elmo.move(piec);
			move(num);
			repaint();
		}

		if (e.getActionCommand().equals("random")) {

			int num;
			while (legal == false) {
				System.out.println("legal");
				num = MrV.move(piec);
				if (piec[num].isAlive == true) {
					legal = true;
					move(num);
				}
			}
			legal = false;

			repaint();
		}
	}

	public void move(int z) {
		notLegal(piec[z], z);
		for (int q = 0; q < 100; q++) {
			if ((piec[z].xpos <= piec[q].xpos) && (piec[z].ypos >= piec[q].ypos)) {
				piec[q].isAlive = false;
			}
		}
		if (youLose == true) {
			System.out.println(loser + "  is the loser");
		}
	}

	public void notLegal(Chip chip, int chipNum) {
		if (chip.isAlive == false) {
			youLose = true;
		}
		if (chipNum == 9) {
			youLose = true;
		}
	}

	public void update(Graphics g) {
		paint(g);
	}

	public void paint(Graphics g) {
		if (youLose) {
			g.setColor(Color.black);
			g.fillRect(0, 0, 600, 600);
			g.setColor(Color.red);
			g.drawString("YOU LOSE ", 100, 100);
		}
		if (youLose == false) {
			chipNum = 0;
			g.setColor(Color.lightGray);
			g.fillRect(15, 15 + 20, CELL_WIDTH * NUM_ROWS, CELL_WIDTH * NUM_ROWS);
			g.setColor(Color.black);
			g.drawRect(10, 10 + 20, CELL_WIDTH * NUM_ROWS + 10, CELL_WIDTH * NUM_ROWS + 10);
			for (int c = 0; c < NUM_ROWS; c++)
				for (int r = 0; r < NUM_ROWS; r++)
					g.drawRect(15 + CELL_WIDTH * c, 15 + 20 + CELL_WIDTH * r, CELL_WIDTH, CELL_WIDTH);

			for (int i = 0; i < 100; i++) {

				g.setColor(Color.red);

				if (piec[i].isAlive) {
					g.fillOval(piec[i].xpos, piec[i].ypos, CELL_WIDTH - 6, CELL_WIDTH - 6);
					g.setColor(Color.blue);
					g.drawOval(piec[i].xpos, piec[i].ypos, CELL_WIDTH - 6, CELL_WIDTH - 6);
					g.setColor(Color.red);

					g.setColor(Color.blue);
					if (piec[9].isAlive)
						g.fillOval(piec[9].xpos, piec[9].ypos, CELL_WIDTH - 6, CELL_WIDTH - 6);
				}
			}
		}
	}
}


