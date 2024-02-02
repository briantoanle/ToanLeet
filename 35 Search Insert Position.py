

             #
# [1,2,3,4,5,6,7,8,9,15]
# find 3

# split half index[5] = 6

def searchInsertPosition(arr,target):

    arrLength = len(arr)-1
    low,high = 0, arrLength
    # mid = (low + (high - low)) // 2
    # mid = (low + high) // 2
    while low <= high:
        # mid = (low + (high - low)) // 2
        mid = (low + high) // 2
        print("mid =", mid)

        if target == arr[mid]:
            return mid
        # if target > arr[mid]:
        #     low = mid + 1
        #     print('low',low,high)
        # elif target < arr[mid]:
        #     high = mid - 1
        #     print('high')
        if arr[mid] < target:
            low = mid + 1
            print("low increment")
        else:
            high = mid - 1
            print("high decrement")

        # if low >= high:
        #     print('not found', low, high)
        #     break
    return low
def testcase1():
    nums = [1, 3, 5, 6, 8]
    target = 0
    #output = 2

    print(searchInsertPosition(nums,target))
testcase1()

def testcase2():
    nums = [1, 3, 5, 6]
    target = 2
    # output = 1

    searchInsertPosition(nums, target)


#print(searchInsertPosition(nums,target))