import random
def init():
    board =[]
    for i in range(4):
        board.append([0] * 4)
    print("Commands are as follows : ")
    print("1 : Move Left")
    print("2 : Move Right")
    print("3 : Move Up")
    print("4 : Move Down")
    addRandom(board)
    return board

def addRandom(board):
    number=[2,4][random.randint(0,1)]
    row = random.randint(0, 3)
    col = random.randint(0, 3)
    d={}
    while(board[row][col] != 0):
        row = random.randint(0, 3)
        col = random.randint(0, 3)
        if row not in d:
            d[row]={col}
        else:
            d[row].add(col)
        bre=False
        if len(d)==4:
            bre=True
            for i in d:
                if len(d[i])!=4:
                    bre=False
        if bre:
            break

    board[row][col]=number

def getGameState(board):
    # 1 for win -1 for lost 0 
	for i in range(4):
		for j in range(4):
			if(board[i][j]== 2048):
				return 1
	# if we are still left with
    # atleast one empty cell
    # game is not yet over
	for i in range(4):
		for j in range(4):
			if(board[i][j]== 0):
				return 0
	# or if no cell is empty now
    # but if after any move left, right,
    # up or down, if any two cells
    # gets merged and create an empty
    # cell then also game is not yet over
	for i in range(3):
		for j in range(3):
			if(board[i][j]== board[i + 1][j] or board[i][j]== board[i][j + 1]):
				return 0
	for j in range(3):
		if(board[3][j]== board[3][j + 1]):
			return 0
	for i in range(3):
		if(board[i][3]== board[i + 1][3]):
			return 0
	return -1

def compress(board):
	# bool variable to determine
	# any change happened or not
	changed = False
	# empty grid
	newBoard = []
	# with all cells empty
	for i in range(4):
		newBoard.append([0] * 4)
	# here we will shift entries
	# of each cell to it's extreme
	# left row by row
	# loop to traverse rows
	for i in range(4):
		pos = 0
		# loop to traverse each column
		# in respective row
		for j in range(4):
			if(board[i][j] != 0):
				# if cell is non empty then
				# we will shift it's number to
				# previous empty cell in that row
				# denoted by pos variable
				newBoard[i][pos] = board[i][j]
				if(j != pos):
					changed = True
				pos += 1
	# returning new compressed matrix
	# and the flag variable.
	return newBoard, changed

# function to merge the cells
# in matrix after compressing
def merge(board):	
	changed = False	
	for i in range(4):
		for j in range(3):
			# if current cell has same value as
			# next cell in the row and they
			# are non empty then
			if(board[i][j] == board[i][j + 1] and board[i][j] != 0):
				# double current cell value and
				# empty the next cell
				board[i][j] = board[i][j] * 2
				board[i][j + 1] = 0
				# make bool variable True indicating
				# the new grid after merging is
				# different.
				changed = True

	return board, changed

# function to reverse the matrix
# maens reversing the content of
# each row (reversing the sequence)
def reverse(board):
	newBoard =[]
	for i in range(4):
		newBoard.append([])
		for j in range(4):
			newBoard[i].append(board[i][3 - j])
	return newBoard

# function to get the transpose
# of matrix means interchanging
# rows and column
def transpose(board):
	newBoard = []
	for i in range(4):
		newBoard.append([])
		for j in range(4):
			newBoard[i].append(board[j][i])
	return newBoard

def moveLeft(grid):
	# first compress the grid
	newGrid, changed1 = compress(grid)
	# then merge the cells.
	newGrid, changed2 = merge(newGrid)
	changed = changed1 or changed2
	# again compress after merging.
	newGrid, temp = compress(newGrid)
	# return new matrix and bool changed
	# telling whether the grid is same
	# or different
	return newGrid, changed

def moveRight(grid):
	# to move right we just reverse
	# the matrix
	newGrid = reverse(grid)
	# then move left
	newGrid, changed = moveLeft(newGrid)
	# then again reverse matrix will
	# give us desired result
	newGrid = reverse(newGrid)
	return newGrid, changed

def moveUp(grid):
	# to move up we just take
	# transpose of matrix
	newGrid = transpose(grid)
	# then move left (calling all
	# included functions) then
	newGrid, changed = moveLeft(newGrid)
	# again take transpose will give
	# desired results
	newGrid = transpose(newGrid)
	return newGrid, changed

def moveDown(grid):
	# to move down we take transpose
	newGrid = transpose(grid)
	# move right and then again
	newGrid, changed = moveRight(newGrid)
	# take transpose will give desired results.
	newGrid = transpose(newGrid)
	return newGrid, changed

def printBoard(board):
	for row in board:
		for val in row:
			print(str(val).center(4),end=" ")
		print()

mat=init()

while(True):
    printBoard(mat)
    x = input("Press the command : ")
    # we have to move up
    if(x == '3'):
		# call the move_up function
        mat, flag = moveUp(mat)
		# get the current state and print it
        status = getGameState(mat)
        if(status == 0):
            addRandom(mat)
        else:
            if status==1:
                print("WON")
            else:
                print("LOST")
            break

	# the above process will be followed
	# in case of each type of move
	# below
	# to move down
    elif(x == '4'):
        mat, flag = moveDown(mat)
        status = getGameState(mat)
        if(status == 0):
            addRandom(mat)
        else:
            if status==1:
                print("WON")
            else:
                print("LOST")
            break

	# to move left
    elif(x == '1'):
        mat, flag = moveLeft(mat)
        status = getGameState(mat)
        if(status == 0):
            addRandom(mat)
        else:
            if status==1:
                print("WON")
            else:
                print("LOST")
            break
	# to move right
    elif(x == '2'):
        mat, flag = moveRight(mat)
        status = getGameState(mat)
        if(status == 0):
            addRandom(mat)
        else:
            if status==1:
                print("WON")
            else:
                print("LOST")
            break
    else:
        print("Invalid Key Pressed")
    
