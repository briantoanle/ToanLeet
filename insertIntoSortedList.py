import math


class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

def toString(head):
    temp = head
    s = ''
    while temp:
        s += str(temp.val) + ' -> '
        temp = temp.next
    return s

# node is 1 3 4 7
def insert(head,value):

    temp = head
    '''if temp.next == None:
        print('here')
        temp.next = ListNode(value)
        return head
    print(toString(head))'''
    # travel to 4
    while temp:
        if temp.val <= value and temp.next.val > value:
            break
        temp = temp.next
    # make a new listnode
    newVal = ListNode(value)
    # set the 5 before 7
    newVal.next = temp.next

    # set 4's next to 5
    temp.next = newVal
    return head

def remove(head,value):
    temp = head
    while temp:
        if temp.next.val == value:
            break
        temp = temp.next
    print(temp.val)
    temp.next = temp.next.next
    return head

def removeDuplicate(head):
    temp = head
    while temp:
        if temp.val == temp.next.val:
            print('here')
            temp.next = temp.next.next
        temp = temp.next
        #print(toString(head))
    return head

# remove all instances of an element in the linked list

def removeElement(head,value):
    temp = ListNode(0,head)
    x = temp
    while temp.next:
        #print('currently at',temp.val)
        print('checking',temp.next.val)
        if temp.next.val == value:

            print('removing',value)
            temp.next = temp.next.next
        else:
            temp = temp.next
        print('current node',toString(head))
        print(toString(x),'*****')
    return x.next

# 876
def middleOfList(head):
    counter = 0
    temp = head
    x = head
    while temp:
        counter+=1
        temp = temp.next
    if counter % 2 == 0:
        distance = int(counter/2)
        for i in range(distance):
            x = x.next
    else:
        distance = counter//2
        for i in range(distance):
            x = x.next
    print(toString(x))
    print(counter)
head = ListNode(7)
head.next = ListNode(7)
head.next.next = ListNode(7)
head.next.next.next = ListNode(7)
head.next.next.next.next = ListNode(4)
#head.next.next.next.next.next = ListNode(6)
#print(toString(head))
#removeDuplicate(head)

#head = removeElement(head,7)
middleOfList(head)
print(toString(head))


