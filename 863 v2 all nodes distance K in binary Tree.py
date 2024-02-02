# use levelOrderTraversal.py to break problem down

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return "toan" + str(self.val)

node3 = TreeNode(3)
node5 = TreeNode(5)
node1 = TreeNode(1)
node6 = TreeNode(6)
node2 = TreeNode(2)
node0 = TreeNode(0)
node8 = TreeNode(8)
node7 = TreeNode(7)
node4 = TreeNode(4)
node9 = TreeNode(9)
node11 = TreeNode(11)

node3.left = node5
node3.right = node1
node5.left = node6
node5.right = node2
node1.left = node0
node1.right = node8
node2.left = node7
node2.right = node4
node0.left = None
node0.right = None
node8.left = node9
node4.right = node11

def printTree(root, level):
    if root is not None:
        printTree(root.right, level + 1)

        for i in range(0, level):
            print("\t", end="")
        print(root.val)
        printTree(root.left, level + 1)

def levelOrder(root):
    final_list = []

    queue = []
    queue.append(root)

    while len(queue) > 0:
        #print(queue)
        for i in range(len(queue)):
            currentNode = queue.pop(0)
            #print('()', currentNode)
            if currentNode.left is not None:
                final_list.append([currentNode, currentNode.left])
                #print('*', currentNode.left)
                queue.append(currentNode.left)
            if currentNode.right is not None:
                final_list.append([currentNode, currentNode.right])
                #print('-', currentNode.right)
                queue.append(currentNode.right)
    return final_list

def queue_to_dictionary(root):
    queue = levelOrder(root)

    dict = {}
    for i in queue:
        if i[0].val not in dict:
            dict[i[0].val] = [i[1].val]
        else:
            dict[i[0].val].append(i[1].val)
        if i[1].val not in dict:
            dict[i[1].val] = [i[0].val]
        else:
            dict[i[1].val].append(i[0].val)
    #print(dict)
    return dict
def findNodesWithinDistanceK(root,target,k):
    dict = queue_to_dictionary(root)

    if not dict:

        return []
    visited = set()
    visited.add(target.val)
    travelQueue = [target.val]
    while k > 0:
        size = len(travelQueue)
        for i in range(size):
            currentNode = travelQueue.pop(0)
            connections = dict[currentNode]

            for n in connections:
                if n not in visited:
                    travelQueue.append(n)
                    visited.add(n)

        k -= 1
    return travelQueue

printTree(node3,0)
#node20 = TreeNode(20)
print(findNodesWithinDistanceK(node3,node5,2))