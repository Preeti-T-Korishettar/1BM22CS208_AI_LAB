#8_QUEENS
from random import randint

N = 8

def configure(board, state):

   state[0]=4
   state[1]=5
   state[2]=6
   state[3]=3
   state[4]=4
   state[5]=5
   state[6]=6
   state[7]=5
   for i in range(N):
    board[state[i]][i] = 1;
   #state[i] = randint(0, 100000) % N;

def printBoard(board):
	for i in range(N):
		print(board[i])

def printState( state):
	print(state)

def compareStates(state1, state2):


	for i in range(N):
		if (state1[i] != state2[i]):
			return False;

	return True;

def fill(board, value):

	for i in range(N):
		for j in range(N):
			board[i][j] = value;

def calculateObjective( board, state):

	attacking = 0;

	for i in range(N):
		# To the left of same row
		# (row remains constant
		# and col decreases)
		row = state[i]
		col = i - 1;
		while (col >= 0 and board[row][col] != 1) :
			col -= 1

		if (col >= 0 and board[row][col] == 1) :
			attacking += 1;

		# To the right of same row
		# (row remains constant
		# and col increases)
		row = state[i]
		col = i + 1;
		while (col < N and board[row][col] != 1):
			col += 1;

		if (col < N and board[row][col] == 1) :
			attacking += 1;

		# Diagonally to the left up
		# (row and col simultaneously
		# decrease)
		row = state[i] - 1
		col = i - 1;
		while (col >= 0 and row >= 0 and board[row][col] != 1) :
			col-= 1;
			row-= 1;

		if (col >= 0 and row >= 0 and board[row][col] == 1) :
			attacking+= 1;

		# Diagonally to the right down
		# (row and col simultaneously
		# increase)
		row = state[i] + 1
		col = i + 1;
		while (col < N and row < N and board[row][col] != 1) :
			col+= 1;
			row+= 1;

		if (col < N and row < N and board[row][col] == 1) :
			attacking += 1;

		# Diagonally to the left down
		# (col decreases and row
		# increases)
		row = state[i] + 1
		col = i - 1;
		while (col >= 0 and row < N and board[row][col] != 1) :
			col -= 1;
			row += 1;

		if (col >= 0 and row < N and board[row][col] == 1) :
			attacking += 1;

		# Diagonally to the right up
		# (col increases and row
		# decreases)
		row = state[i] - 1
		col = i + 1;
		while (col < N and row >= 0 and board[row][col] != 1) :
			col += 1;
			row -= 1;

		if (col < N and row >= 0 and board[row][col] == 1) :
			attacking += 1;

	return int(attacking / 2);

def generateBoard( board, state):
	fill(board, 0);
	for i in range(N):
		board[state[i]][i] = 1;

def copyState( state1, state2):

	for i in range(N):
		state1[i] = state2[i];

def getNeighbour(board, state):

	opBoard = [[0 for _ in range(N)] for _ in range(N)]
	opState = [0 for _ in range(N)]

	copyState(opState, state);
	generateBoard(opBoard, opState);

	opObjective = calculateObjective(opBoard, opState);

	NeighbourBoard = [[0 for _ in range(N)] for _ in range(N)]

	NeighbourState = [0 for _ in range(N)]
	copyState(NeighbourState, state);
	generateBoard(NeighbourBoard, NeighbourState);

	for i in range(N):
		for j in range(N):

			if (j != state[i]) :
				NeighbourState[i] = j;
				NeighbourBoard[NeighbourState[i]][i] = 1;
				NeighbourBoard[state[i]][i] = 0;
				temp = calculateObjective( NeighbourBoard, NeighbourState);


				if (temp <= opObjective) :
					opObjective = temp;
					copyState(opState, NeighbourState);
					generateBoard(opBoard, opState);

				NeighbourBoard[NeighbourState[i]][i] = 0;
				NeighbourState[i] = state[i];
				NeighbourBoard[state[i]][i] = 1;
	print(opState," ",opObjective)
	copyState(state, opState);
	fill(board, 0);
	generateBoard(board, state);

def hillClimbing(board, state):

	neighbourBoard = [[0 for _ in range(N)] for _ in range(N)]
	neighbourState = [0 for _ in range(N)]

	copyState(neighbourState, state);
	generateBoard(neighbourBoard, neighbourState);

	while True:
		copyState(state, neighbourState);
		generateBoard(board, state);
		getNeighbour(neighbourBoard, neighbourState);

		if (compareStates(state, neighbourState)) :
			printBoard(board);print(state);
			break;

		elif (calculateObjective(board, state) == calculateObjective( neighbourBoard,neighbourState)):
			neighbourState[randint(0, 100000) % N] = randint(0, 100000) % N;
			generateBoard(neighbourBoard, neighbourState);


state = [0] * N
board = [[0 for _ in range(N)] for _ in range(N)]

configure(board, state);

hillClimbing(board, state);
