test_list1 = [1, 5, 6, 9, 11]
test_list2 = [3, 4, 7, 8,10]

def median(test_list1,test_list2):

    nl = sorted(test_list1+test_list2)
    print(nl)
    mid = len(nl)//2
    print(mid)
    if len(nl)%2 ==1:
        return nl[mid]
    if len(nl) % 2 == 0:
        return (nl[mid]+nl[mid-1])/2
print(median(test_list1,test_list2))