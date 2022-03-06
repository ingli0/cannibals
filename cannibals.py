import copy
from tkinter import N
POSSIBLE_ACTIONS = [[1,1],[0,2],[2,0],[0,1],[1,0]]

class State():
	
	def __init__(self, aristera, barka, deksia):
		self.aristera=aristera;
		self.barka = barka;
		self.deksia=deksia;
		self.prev = None
		
	def _str__(self):
		return("({},{}) - ({},{}) - {}".format(self.aristera[0],self.aristera[1],self.deksia[0],self.deksia[1],self.barka))
	
	def isValidState(self):	
		# ama oi kanibaloi einai perisoteroi apo tous ierapostolous on the aristera or deksia side
		if(0 < self.aristera[0] < self.aristera[1] or 0 < self.deksia[0] < self.deksia[1]):
			return False	
		#se periptosi pou metaferthoun parpanw apo to sunolo ton atomon pou uparxoun
		if(self.aristera[0]<0 or self.aristera[1]<0 or self.deksia[0]<0 or self.deksia[1]<0):
			return False
		
		
		return True

	def __eq__(self, other):
		return (self.aristera[0]==other.aristera[0] and self.aristera[1] == other.aristera[1] and self.deksia[0]==other.deksia[0] and self.deksia[1]==other.deksia[1] and self.barka==other.barka)
		
	def __hash__(self):
		return hash((self.aristera[0],self.aristera[1],self.barka,self.deksia[0],self.deksia[1]))
	
	def _str_(self):
		return("({},{}) - ({},{}) - {}".format(self.aristera[0],self.aristera[1],self.deksia[0],self.deksia[1],self.barka))
	
	def isGoalState(self):
		# to state pou theloume na ftasoume dhladi aloi oi kanibaloi kai oi ierapostoloi na pane stin apenanti oxthi
		return(self.aristera[0]==0 and self.aristera[1]==0)

def nextStates(current):
	nodes=[]

	for action in POSSIBLE_ACTIONS:
		
		nextState = copy.deepcopy(current)
		nextState.prev=current
		
		# h barka tha paei stin antitheti pleura
		nextState.barka = 1-current.barka
		
		# metakinisi apo aristera pros ta deksia
		if(current.barka==0):

			#auksisi twn atomwn sthn deksia oxthi
			nextState.deksia[0]+=action[0]
			nextState.deksia[1]+=action[1]
			
			#miosi twn atomwn sthn aristera oxthi
			nextState.aristera[0]-=action[0]
			nextState.aristera[1]-=action[1]
		
		#metakisni apo  deksia pros ta aristera
		elif(current.barka==1):
			
			#miosi twn atomwn sthn deksia oxthi
			nextState.deksia[0]-=action[0]
			nextState.deksia[1]-=action[1]
			
			#auksisi twn atomwn sthn aristera oxthi
			nextState.aristera[0]+=action[0]
			nextState.aristera[1]+=action[1]
		
		if nextState.isValidState():
			nodes.append(nextState)

	return nodes
	
def bfs(root):
	
	if root.isGoalState():
		return root
	
	visited = set()
	queue = [root]

	while queue:
		state = queue.pop()
		if state.isGoalState():
			return state
		
		visited.add(state)
		
		for child in nextStates(state):
			if child in visited:
				continue

			if child not in queue:
				queue.append(child)

def main():
	initial_state = State([3,3],0,[0,0])
	state = bfs(initial_state)
	
	#path
	path=[]
	while state:
		path.append(state)
		state = state.prev
		
	
	#antistrofh tou path
	path.reverse()
	
	#anaparastasi tou algorithmou
	for state in path:
		if state.barka:
			print("""{:3} ||         b|| {:3}\n{:3} ||          || {:3}""".format("K"*state.aristera[1], "K"*state.deksia[1], "I"*state.aristera[0], "I"*state.deksia[0]))
		else:
			print("""{:3} ||b         || {:3}\n{:3} ||          || {:3}""".format("K"*state.aristera[1], "K"*state.deksia[1], "I"*state.aristera[0], "I"*state.deksia[0]))
		print("\n")

if __name__ == "__main__":
	main()