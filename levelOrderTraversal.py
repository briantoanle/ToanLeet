class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


'''
                1
            /       \
        2               3
    /       \       /       \
    4       5       6       7
'''
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7


def print_level_order_traversal(root):
    final_list = []

    queue = []
    queue.append(root)

    while len(queue) > 0:
        print(queue)
        for i in range(len(queue)):
            currentNode = queue.pop(0)
            print('()',currentNode)
            if currentNode.left is not None:
                final_list.append([currentNode,currentNode.left])
                print('*', currentNode.left)
                queue.append(currentNode.left)
            if currentNode.right is not None:
                final_list.append([currentNode, currentNode.right])
                print('-',currentNode.right)
                queue.append(currentNode.right)
    print(final_list)
print(print_level_order_traversal(node1))