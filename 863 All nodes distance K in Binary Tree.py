class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return "t" + str(self.val)

def printTree(root, level):
    if root is not None:
        printTree(root.right, level + 1)

        for i in range(0, level):
            print("\t", end="")
        print(root.val)
        printTree(root.left, level + 1)


node3 = TreeNode(3)
node5 = TreeNode(5)
node1 = TreeNode(1)
node6 = TreeNode(6)
node2 = TreeNode(2)
node0 = TreeNode(0)
node8 = TreeNode(8)
node7 = TreeNode(7)
node4 = TreeNode(4)

node3.left = node5
node3.right = node1
node5.left = node6
node5.right = node2
node1.left = node0
node1.right = node8
node2.left = node7
node2.right = node4

'''
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
'''

def levelOrderTraversal(root):

    levels = []
    fullTree = []
    levels.append(root)
    levels.append(root.left)
    levels.append(root.right)

    run = True

    masterList = []
    masterList.append([root,root.left])
    masterList.append([root, root.right])

    while run:

        fullTree.append(levels.pop(0))
        if(levels[0].left != None):
            masterList.append([levels[0],levels[0].left])
            levels.append(levels[0].left)
        if(levels[0].right != None):
            masterList.append([levels[0], levels[0].right])
            levels.append(levels[0].right)
        if(len(levels) == 1):
            fullTree.append(levels[0])
            run = False
    return masterList

def arrayToDictionary(root):
    masterList = levelOrderTraversal(root)
    print(masterList)
    dict = {}
    for i in masterList:
        if i[0] not in dict:
            dict[i[0]] = [i[1]]
        else:
            dict[i[0]].append(i[1])
        if i[1] not in dict:
            dict[i[1]] = [i[0]]
        else:
            dict[i[1]].append(i[0])
    return dict
def findNodesWithinDistanceK(root,target,k):
    dict = arrayToDictionary(root)
    visited = set()
    visited.add(target)
    travelQueue = [target]
    while k > 0:
        size = len(travelQueue)
        for i in range(size):
            currentNode = travelQueue.pop(0)
            connections = dict[currentNode]
            print(connections)
            for n in connections:
                if n not in visited:
                    travelQueue.append(n)
                    visited.add(n)

        k -= 1
    return travelQueue
    # starting = dict[target]

    # :
    #     print(starting)
    #    for


    #print(dict)
#printTree(node3,0)
#levelOrderTraversal(node3)

# [3, 5]
# [3, 1]
# [5, 6]
# [5, 2]
# [1, 0]
# [1, 8]
# [2, 7]
# [2, 4]

node10 = TreeNode(10)
print(findNodesWithinDistanceK(node3,node3,1))

