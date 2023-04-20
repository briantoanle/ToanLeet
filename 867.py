matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

matrix1 = [[1,2,3],[4,5,6]]
testCase1 = [[2,-10,18],
             [4,5,-7],
             [-1,11,6]]

def transpose(matrix):
    #temp = [[None]*len(matrix)]*len(matrix[0])
    lenI = len(matrix[0])
    lenJ = len(matrix)
    temp = []
    for i in range(lenI):
        temp.append([None]*lenJ)
    print(temp)
    for i in range(lenI):
        for j in range(lenJ):
            temp[i][j] = matrix[j][i]
    print(temp)
transpose(matrix1)

#21,206,83