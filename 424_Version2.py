s = 'AABABBACBCCBACCCA'
z = 'ASDHKJHO'
l = 'LAJALKAA'
k = 2

'''
easy = 'AABBABABBA'
lst = [0] * 26
print(lst)
print(ord('B') - 65)

for c in easy:
    lst[ord(c)-65] +=1

print(lst)

c = 'A'
lst[ord(c) - 65] -= 1
print(lst)
'''
'''def solution(array, repeats):
    lst = [0] * 26

    left = 0
    right = 0
    while right < len(array):

        print(array[left:right+1])

        lst[ord(array[right])-65] +=1

        temp = array[left:right+1]

        print(lst)
        if len(temp) - max(lst) <= repeats:
            print('valid',len(temp),max(lst), 'sum: ',len(temp)-max(lst))
        else:
            lst[ord(array[left]) - 65] -= 1
            left+=1

        right+=1'''

def solution(array, repeats):
    lst = [0] * 26

    left = 0
    right = 0
    final = 0
    while right < len(array):

        lst[ord(array[right])-65] +=1

        temp = array[left:right+1]
        if len(temp) - max(lst) <= repeats:

            final = len(temp)
        else:
            lst[ord(array[left]) - 65] -= 1
            left+=1

        right+=1
    return final

print(solution(s,2))
