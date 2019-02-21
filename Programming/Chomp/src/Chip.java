import java.applet.*;
import java.awt.*;
import java.awt.event.*;
import java.util.*;


public class Chip{

		 public int xpos,ypos;
		 public Rectangle myRect;
		 public boolean isAlive;
		 public int chipNum;

		 public Chip(int x,int y,int z){
			 chipNum=z;
			 isAlive=true;
			 xpos=x;
			 ypos=y;
			 myRect=new Rectangle(xpos,ypos,24,24);
		 }

	 }