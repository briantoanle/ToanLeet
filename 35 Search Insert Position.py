nums = [1]

target = 2

def searchInsertPosition(arr,target):
    last = len(arr)
    if target < arr[0] a last == 1 :

        return 0
    elif target > arr[0] and last == 1:
        return 1
    for i in range(last - 1):
        if arr[i] == target:
            return i
        elif arr[i] < target and arr[i + 1] > target:
            return i + 1
    return last

print(searchInsertPosition(nums,target))