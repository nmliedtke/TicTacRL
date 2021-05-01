from tensorforce.environments import Environment

class TicTacEnv(Environment):
	board = 
	def __init__(self):
		self.boardState  =[0,0,0,0,0,0,0,0,0]
		self.turnsTaken==0
		self.turn = 2
        super().__init__()
		
	def states(self):
        return dict(type='int', shape=9, num_states=3)

    def actions(self):
        return dict(type='int', num_actions = 9)
		
	def max_episode_timesteps(self):
        return 9
		
	def close(self):
        super().close()
		
	def reset(self):
		self.boardState  =[0,0,0,0,0,0,0,0,0]
		self.turnsTaken = 0
		self.turn = 1
        return self.boardState

    def execute(self, act):
        # check if illegal move
		if self.boardState[act] != 0:
			return self.boardState, True, 0.0, 'illegal'
		self.boardState[act] = self.turn
		self.turnsTaken += 1
		self.turn = (self.turnsTaken%2)+1
		# toggle self.turn
		self.turn = 2 if self.turn == 1 else self.turn = 1
		if self.checkWinner():
			return self.boardState, True, 1.0, 'win'
		if self.turnsTaken >= self.max_episode_timesteps():
			return self.boardState, True, 0.5, 'draw'
			
		
		return self.boardState, False, 0.02, 'turn'
		
	def checkWinner():
		winner = false
		b = self.boardState
		# check  rows
		for row in [0,3,6]
			if b[row] == b[row+1] == b[row+2]:
				return True
		# check cols
		for col in [0,1,2]
			if b[col] == b[col+3] ==b[col+6]:
				return True
				
		#check diags
		if b[0] == b[4] == b[8]:
			return True
		if b[2]==b[4]==b[6]:
			return True
		return False