class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node4
newNode1 = ListNode(1)
newNode4 = ListNode(4)

newNode1.next = node3
node3.next = newNode4

def printAListNode(node1):
    temp = node1

    while temp:
        print(temp.val,end= " ")
        temp = temp.next

printAListNode(node1)
print()
printAListNode(newNode1)

# creating another list
def mergeSortedList(l1,l2):
    output = ListNode(None)
    l1c = l1
    l2c = l2
    while l1c:
        

mergeSortedList(node1,newNode1)