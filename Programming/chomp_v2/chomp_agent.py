import random

import numpy as np


class ChompAgent:
	def __init__(self, epsilon_greedy=0.1, learning_rate=0.5, discount_factor=0.01):
		self.states = {}
		self.state_order = []
		self.learning_rate = learning_rate
		self.discount_factor = discount_factor
		self.epsilon_greedy = epsilon_greedy

	def get_serious(self):
		self.epsilon_greedy = 1

	def learn_by_temporal_difference(self, board, reward, new_state_key, state_key):
		old_state = self.states.get(state_key, np.zeros((board.size, board.size)))
		return self.learning_rate * ((reward * self.states[new_state_key]) - old_state)

	def set_state(self, old_board, action):
		state_key = old_board.serialize()
		self.state_order.append((state_key, action))

	def on_reward(self, board, reward):
		if len(self.state_order) == 0:
			return

		new_state_key, new_action = self.state_order.pop()
		# get the latest state and the action performed that led to the reward

		self.states[new_state_key] = np.zeros((board.size, board.size))
		# initialize the value with a zero matrix

		self.states[new_state_key].itemset(new_action, reward)
		# Assign the reward to this state

		while self.state_order:
			# while there is a stack of states (that were caused by actions performed)

			state_key, action = self.state_order.pop()
			# get the state and action performed on it

			reward *= self.discount_factor
			# Reduce the original reward (self.discount_factor is a number < 1)

			# Implementation of the value function
			if state_key in self.states:
				reward += self.learn_by_temporal_difference(board, reward, new_state_key, state_key).item(new_action)
				# If this state was encountered due to a different experiment, increase its previous value
				self.states[state_key].itemset(action, reward)
			else:
				self.states[state_key] = np.zeros((board.size, board.size))
				reward = self.learn_by_temporal_difference(board, reward, new_state_key, state_key).item(new_action)
				self.states[state_key].itemset(action, reward)
			# If this state was not encountered before, assign it the discounted reward as its value
			new_state_key = state_key
			new_action = action

	def select_move(self, board):
		state_key = board.serialize()
		exploitation = np.random.random() < self.epsilon_greedy
		action = self.explore_board(board) \
			if not exploitation or state_key not in self.states \
			else self.exploit_board(board, state_key)
		self.set_state(board, action)
		print(('Explore: ' if not exploitation or state_key not in self.states else 'Exploit: ') + str(action))
		return action

	@staticmethod
	def explore_board(board):
		moves = board.get_possible_moves()
		move = random.choice(moves)
		return move

	def exploit_board(self, board, state_key):
		state_values = self.states[state_key]
		moves = board.get_possible_moves()
		order = list(map(lambda x: tuple(reversed(np.unravel_index(x, (board.size, board.size)))),
			reversed(np.argsort(state_values, axis=None))))

		for move in order:
			if move in moves:
				return move

	def summarize_training(self):
		np.set_printoptions(precision=3)
		for state in self.states:
			q_values = self.states[state]
			print('state: ' + state)
			print(q_values)
