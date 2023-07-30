def removeDuplicates(num):
    print(num)
    left = 0
    counter = 1

    for right in range(1,len(num)):
        print("left", left, "right", right)
        print("value of left", num[left], "value of right", num[right])
        if num[left] == num[right]:
            if counter < 2:
                print('swapping')
                num[left] = num[right]
                left += 1
            counter += 1
        else:
            left += 1
            print('swapping index' , left, 'and',right)
            num[left] = num[right]
            counter = 1
            print('swapped')

        print('*********',num)



    print(num)

    return num

def removeDuplicates2(num):
    left = 0
    counter = 1
    for right in range(1,len(num)):
        if num[left] == num[right]:
            if counter < 2:
                left += 1
                num[left] = num[right]
                counter += 1

        else:
            left += 1
            num[left] = num[right]
            counter = 1
    return left + 1
arr = [0,0,1,1,1,1,2,3,3]
arr1 = [0,0,0,1,1,2,2,2,3,3,4,4,4,4,5,5,5]
print(removeDuplicates2(arr))