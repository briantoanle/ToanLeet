'''
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down.
You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

'''

class GraphNode:
    def __init__(self,index,name):
        self.index = index
        self.name = name

    def __str__(self):
        return str(self.index) + ""
class GraphEdge:
    def __init__(self,p1,p2):
        self.startingNode = p1
        self.endingNode = p2
        self.distance = 1

    def __repr__(self):
        return str(self.startingNode) + " -> " + str(self.endingNode)
class Graph:
    arr = []
    adjacencyList = {}

    def __init__(self,matrix):
        height = len(matrix)
        width = len(matrix[0])

        # make a new list of graph nodes
        for i in range(height):
            for j in range(width):
                self.arr.append(GraphNode((i*height)+ j, matrix[i][j]))

        # make an adjacency list of graph edge depending on the condition
        moves = [-1,0],[0,1],[0,-1],[1,0]
        for i in range(height):
            for j in range(width):
                temp = matrix[i][j]
                for k in moves:
                    if i - k[0] >= 0 and i - k[0] < height:
                        if j - k[1] >= 0 and j - k[1] < width:
                            destination = (i - k[0]) * height + (j - k[1])
                            destinationName = matrix[i - k[0]][j - k[1]]
                            if temp < destinationName:
                                #print(temp, matrix[i-k[0]][j-k[1]])
                                nodeIndex = ((i*height) + j)
                                if nodeIndex not in self.adjacencyList:
                                    self.adjacencyList[nodeIndex] = []
                                    self.adjacencyList[nodeIndex].append(GraphEdge(GraphNode(nodeIndex,temp),GraphNode(destination,destinationName)))
                                else:
                                    self.adjacencyList[nodeIndex].append(GraphEdge(GraphNode(nodeIndex,temp),GraphNode(destination,destinationName)))

        for i in self.adjacencyList:
            print(self.arr[i],self.adjacencyList[i])

    def findLongestPath(self):



    def __str__(self):
        s = ""
        for i in self.arr:
            s += str(i) + "\n"
        return s



def main():
    matrix = [[9,9,4],[6,6,8],[2,1,1]]
    graph = Graph(matrix)
    #print(graph)

main()