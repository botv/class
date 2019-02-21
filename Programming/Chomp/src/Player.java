public class Player
{
	public int total=0;
	public String name="test";
	public int winNum=0;


	public int move(Chip[] chip)
	{

		for(int x=0;x<100;x++)
		{
			if(chip[x].isAlive)
			{
				total++;
			}


		}
		System.out.println(total);



		if((chip[8].isAlive==true)&&(chip[17].isAlive==false))
		{
			return(8);
		}
		return(11);
	}

}

