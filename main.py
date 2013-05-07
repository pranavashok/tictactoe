import sys
import time

B = {}
for i in range(0, 3):
	for j in range(0, 3):
		B[(i, j)] = " "

def checkWin(B, c):
	for i in range(0, 3):
		row = 1
		for j in range(0, 3):
			if B[(i, j)] != c:
				row = 0
		if row == 1:
			return True
	
	for j in range(0, 3):
		col = 1
		for i in range(0, 3):
			if B[(i, j)] != c:
				col = 0
		if col == 1:
			return True

	dia = 1
	for i in range(0, 3):
		if B[(i, i)] != c:
			dia = 0
	if dia == 1:
		return True

	dia = 1
	for i in range(0, 3):
		j = 2-i
		if B[(i, j)] != c:
			dia = 0
	if dia == 1:
		return True

def computeHeuristic(B):
	count = 0

	#Count free rows
	for i in range(0, 3):
		row = 1
		for j in range(0, 3):
			if B[(i, j)] == "o":
				row = 0
				break
		count += row

	#Count free cols
	for j in range(0, 3):
		col = 1
		for i in range(0, 3):
			if B[(i, j)] == "o":
				col = 0
				break
		count += col

	#Count free diagonals
	for i in range(0, 3):
		dia = 1
		if B[(i, i)] == "o":
			dia = 0
			break
	count += dia

	for i in range(0, 3):
		j = 2 - i
		dia = 1
		if B[(i, j)] == "o":
			dia = 0
			break
	count += dia

	return count

def nextMove(B):
	low = 8
	M = []
	for i in range(0, 3):
		for j in range(0, 3):
			if B[(i, j)] == " ":
				setij(B, i, j, "o")
				h = computeHeuristic(B)
				if h < low:
					low = h
					bestMove = (i, j)
					M = []
					M.append((i, j))
				elif h == low:
					M.append((i, j))
				setij(B, i, j, " ")
	return M

def safeMove(B, M):
	while len(M) > 0:
		move = M.pop()
		B[move] = "x"
		if checkWin(B, "x") == True:
			B[move] = " "
			return move
		B[move] = " "
	return move

def printState(B):
	print(" 1   2   3")
	for i in range(0, 3):
		print(i+1, end="")
		for j in range(0, 3):
			print(B[(i, j)], end="")
			if j < 2:
				print(end=" | ")
		print("")

def setij(B, i, j, c):
	B[(i, j)] = c
	return B

moves = 9
while moves >= 0:
	inp = int(input("Your turn: "))
	row = int(inp/10)
	col = inp%10
	if row <= 3 and row >= 1 and col <=3 and col >= 1:
		if B[(row-1, col-1)] == " ":
			setij(B, row-1, col-1, "x")
		else:
			print("Please enter valid move\n")
			continue
	else:
		print("Please enter valid move\n")
		continue
	moves -= 1
	printState(B)
	if moves == 0:
		print("\nGame drawn\n")
		break
	if checkWin(B, "x"):
		print("\nYou win!\n")
		break
	print("\nComputer's turn.")
	possibleMoves = nextMove(B)
	m = safeMove(B, possibleMoves)
	setij(B, m[0], m[1], "o")
	moves -= 1
	printState(B)
	if moves == 0:
		print("\nGame drawn\n")
		break
	if checkWin(B, "o"):
		print("\nYou lose!\n")
		break
	print("\n")