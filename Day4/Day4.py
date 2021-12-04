f = open("Day4\\Input.txt", "r")

numbers = f.readline().strip().split(",")

boards = []
winnerOrder = []
board = []
marker = "-"

def checkBingo(board):
    rowBingo = False
    colBingo = False
    
    for i in range(len(board)):
        r = True
        c = True
        for j in range(len(board)):
            r = r & (board[i][j]==marker)
            c = c & (board[j][i]==marker)
        rowBingo = rowBingo | r
        colBingo = colBingo | c
    return rowBingo | colBingo

def checkNum(num, board):
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] == num:
                board[r][c] = marker

def printBoard( board ):
    for r in board:
        print( r[0]+" "+r[1]+" "+r[2]+" "+r[3]+" "+r[4])
    print("---------------")

def sumBoard( board ):
    sum = 0
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] != marker:
                sum += int(board[r][c])
    return sum

for s in f:
    if s == "\n":
        if len(board) == 5:
            boards.append(board)
        board = []
    else:
        s = s.strip()
        row = s.split()
        clean = []
        for i in row:
            if len(i)>0:
                clean.append(i)
        board.append( clean )
        

if len(board) == 5:
    boards.append(board)

def part1():
    val = -1
    for num in numbers:
        for i in range(len(boards)):
            b = boards[i]
            checkNum(num,b)
            if checkBingo(b):
                val = sumBoard(b)
                val *= int(num)
                winnerOrder.append(val)
                boards[i] = []
    val = winnerOrder[0]
    print( "Part 1: "+  str(val) )
    printBoard(b)
def part2():
    val = winnerOrder[-1]
    print( "Part 2: "+  str(val) )

part1() 
part2() 