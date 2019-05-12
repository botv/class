import numpy as np
import pandas as pd

from tic_tac_toe_agent import TicTacToeAgent
from tic_tac_toe_board import TicTacToeBoard


def optimize_bot(game, bot1, bot2):
	"""
	Punish or Reward the bot with respect to the agent that wins the game
	"""
	if game.winner == 'O':
		bot1.on_reward(1)
		# reward
		bot2.on_reward(-1)
	# punishment
	elif game.winner == 'X':
		bot1.on_reward(-1)
		bot2.on_reward(1)


def train(epochs, bot1, bot2):
	bots = [{
		'mdl': bot1,
		'name': 'bot1',
		'sym': 'O',
		'wins': 0
	}, {
		'mdl': bot2,
		'name': 'bot2',
		'sym': 'X',
		'wins': 0
	}]

	win_trace = pd.DataFrame(data=np.zeros((epochs, 2)), columns=['bot1', 'bot2'])
	for i in range(epochs):
		print('-' * 100)
		print('epoch: {}'.format(i + 1))
		game = TicTacToeBoard()
		while not game.stale and not game.winner:
			# Exit if the board is full
			for bot in bots:
				winner = game.player_move(bot['sym'], *bot['mdl'].select_move(game.board))
				print('winner found:', winner)
				if winner:
					optimize_bot(game, bot1, bot2)
					bot['wins'] += 1
					win_trace.set_value(i, bot['name'], 1)
					break
				elif winner == 'draw':
					break
	return win_trace, bots[0]['wins'], bots[1]['wins']


def main():
	bot1 = TicTacToeAgent()
	bot2 = TicTacToeAgent()
	epochs = 1000
	win_trace, bot1_wins, bot2_wins = train(epochs, bot1, bot2)
	print(bot1_wins, bot2_wins)
	board = TicTacToeBoard()
	bot = bot2
	board.draw_board()
	bot.get_serious()
	board.play(1, 1)
	board.bot_play(*bot.select_move(board.board))
	board.play(1, 2)
	board.bot_play(*bot.select_move(board.board))
	board.play(0, 1)


if __name__ == '__main__':
	main()
