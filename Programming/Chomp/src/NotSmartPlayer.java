public class NotSmartPlayer extends RandomPlayer
{	public int[] col= new int[10];
	public int total=0;

	public int move(Chip[] chip)
	{
		total=0;
		convCol(chip);



		if(col[0]==col[1] && col[2]==0)
		{

			return(20-col[1]);

		}
		if(col[0]>col[1]+1 && col[2]==0)
		{

			return(10-(2+col[1]));
		}

		return(6);


	}

	public void convCol(Chip[] chip)
	{
		for(int x=0; x<10;x++)
				{col[x]=0;
					for(int z=0; z<10;z++)
					{
						if (chip[total].isAlive)
						{


							col[x]=col[x]+1;
						}
						total=total+1;
					}

				}
	}

}