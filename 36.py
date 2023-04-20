# 36. Valid Sudoku

board =\
[[".",".",".",".","5",".",".","1","."],
 [".","4",".","3",".",".",".",".","."],
 [".",".",".",".",".","3",".",".","1"],
 ["8",".",".",".",".",".",".","2","."],
 [".",".","2",".","7",".",".",".","."],
 [".","1","5",".",".",".",".",".","."],
 [".",".",".",".",".","2",".",".","."],
 [".","2",".","9",".",".",".",".","."],
 [".",".","4",".",".",".",".",".","."]]

def sudoku(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j].isdigit():
                num = board[i][j]
                # check for X axis
                if board[i].count(num) > 1:
                    return False

                # check for Y Axis
                yAxis = []
                for k in range(len(board)):
                    yAxis.append(board[k][j])
                    if yAxis.count(num) > 1:
                        print('here')
                        return False

    for i in range(0,len(board),3):
        for j in range(0,len(board),3):
            box = []
            for k in range(i,i+3):
                for l in range(j,j+3):
                    #print(board[k][l])
                    if board[k][l].isdigit():
                        box.append(board[k][l])
                        if box.count(board[k][l]) >1:
                            return False

    '''for i in range(0,len(board),3):
        #print(i,'i here')
        x1 = []
        x2 = []
        x3 = []
        y=[]

        for j in range(i,i+3):
            #print(j)
            x1.append(board[j][0:3])
            x2.append(board[j][3:6])
            x3.append(board[j][6:9])
            #x1.append(board[j][i:i+3])
        #print(x1)
        #print(x2)
        #print(x3)
        tempList = []
        tempList.append(x1)
        tempList.append(x2)
        tempList.append(x3)

        for k in range(len(tempList)):
            tempBoard = tempList[k]
            #print(tempBoard)
            l1 = []
            for l in range(len(tempBoard)):
                #print(tempBoard[l])
                for m in range(len(tempBoard)):
                    if tempBoard[l][m].isdigit():

                        l1.append(tempBoard[l][m])
                        if l1.count(tempBoard[l][m]) >1:
                            return False
            #print(l1)
            #print('****')'''
    return True

print(sudoku(board))
#print(2//3)