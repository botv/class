class StaticSolver:
	def __init__(self):
		pass

	def act(self, state):
		if state[0][2] > 0:
			return 1
		else:
			return 0
