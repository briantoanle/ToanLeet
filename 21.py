from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(ListNode):
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        print(list1.val)

        return None

    def nodeToList(self,l1):
        arr = []
        while l1:
            arr.append(l1.val)
            l1 = l1.next
        return arr

    def listNodetoString(self, l):
        # print(l.val)
        s = ''
        while l:
            # print('here')
            s += str(l.val) + " "
            l = l.next
        return s

    def listToNode(self,l1):
        ln = ListNode(l1[0])
        ln.next = ListNode(l1[1])
        curr = ln
        for i in range(1,len(l1)):
            curr.next = ListNode(l1[i])
            curr = curr.next
        return ln

    l1 = ListNode(1)
    l1.next = ListNode(2)
    curr = l1.next
    curr.next = ListNode(9)

    l2 = ListNode(4)
    l2.next = ListNode(5)
    l2.next.next = ListNode(6)

    list1 = nodeToList(None,l1)
    list2 = nodeToList(None,l2)
    listMerged = list1+list2
    listSorted = sorted(listMerged)
    print(listSorted)
    print(listNodetoString(None,listToNode(None,listSorted)))
    #mergeTwoLists(None,l1,l2)
    #print(listNodetoString(None,l1))




