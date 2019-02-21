public class SmartPlayer extends NotSmartPlayer
{	public int[] chipN= new int[10];
	public int[] chipRN= new int[10];
	public int total=0;
	public boolean right=true;
	public int lowchip=0;
	public int highchip=99;
	public int hold;
	public int square;

	public int move(Chip[] chip)
	{
	total=0;




		if(chipN[1]==0)
		{System.out.println("1");
		return(8);}

		if(chipRN[1]==0)
		{System.out.println("2");
		return(19);}


		return(9);
	}
}