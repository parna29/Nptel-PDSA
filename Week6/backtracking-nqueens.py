def initialize(board, n):
    for key in ['queen', 'row', 'col', 'nwtose', 'swtone']:
        board[key] = {}
    for i in range(n):
        board['queen'][i] = -1
        board['row'][i] = 0
        board['col'][i] = 0
    for i in range(-(n-1), n):
        board['nwtose'][i] = 0
    for i in range(2*n-1):
        board['swtone'][i] = 0   

def printboard(board):
    for row in sorted(board['queen'].keys()):
        print((row, board['queen'][row]))

def free(i, j, board):
    return(board['row'][i]==0 and board['col'][j]==0 and board['nwtose'][j-i]==0 and board['swtone'][i+j]==0)   

def addqueen(i, j, board):
    board['queen'][i] = j
    board['row'][i] = 1
    board['col'][j] = 1
    board['nwtose'][j-i] = 1
    board['swtone'][i+j] = 1

def undoqueen(i, j, board):
    board['queen'][i] = -1
    board['row'][i] = 0
    board['col'][j] = 0
    board['nwtose'][j-i] = 0
    board['swtone'][i+j] = 0

def placequeen(i, board):
    n = len(board['queen'].keys())
    for j in range(n):
        if free(i, j, board):
            addqueen(i, j, board)
            if i == n-1:
                return(True)
            else:
                extendsoln = placequeen(i+1, board)  
            if extendsoln:
                return(True)
            else:
                undoqueen(i, j, board)
    else:
        return(False) #after running entire for loop, if it doesn't return True, it means not possible to place all queens  

board = {}
n = int(input('How many queens? : '))   
initialize(board, n) #initializing empty board of size n
if placequeen(0, board):
    printboard(board)
