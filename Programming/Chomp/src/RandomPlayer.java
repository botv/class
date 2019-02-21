public class RandomPlayer extends Player
{

	public int total=0;



	public int move(Chip[] chip)
	{

		count(chip);

		return((int)(100.0*Math.random()));
	}

	public void count(Chip[] c)
	{
		total=0;

		for(int x=0; x<100; x++)
		{

			if(c[x].isAlive)
			{
				total++;
			}

		}
		System.out.println(total);
	}

}

