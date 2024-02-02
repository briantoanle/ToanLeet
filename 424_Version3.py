s = 'AABABBACBCCBACCCA'
z = 'ASDHKJHO'
l = 'LAJALKAA'
k = 2


def solution2(array,repeats):
    left, right, final = 0, 0, 0
    dict = {}
    while right < len(array):

        tempChar = array[right]
        if tempChar not in dict:
            dict[tempChar] = 1
        else:
            dict[tempChar] += 1

        tempLen = len(array[left:right + 1])

        tempMax = 0

        for value in dict.values():
            if value > tempMax:
                tempMax = value

        if tempLen - tempMax <= repeats:

            final = tempLen
        else:
            dict[array[left]] -= 1
            left += 1
        right += 1

    return final

def solution(array,repeats):

    left,right,final = 0,0,0
    dict = {}
    while right < len(array):

        tempChar = array[right]
        if tempChar not in dict:
            dict[tempChar] = 1
        else:
            dict[tempChar] += 1

        tempLen = len(array[left:right+1])
        if tempLen - max(dict.values()) <= repeats:
            print('valid')
            final = tempLen
        else:
            dict[array[left]] -= 1
            left += 1
        right +=1

    print(final)

print(solution2(z,0))