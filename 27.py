


def removeElement(arr,val):
    temp = []
    for i in arr:
        if i not in temp and i != val:
            temp.append(i)
    return temp


nums = [3,2,2,3]
val = 3

print(removeElement(nums,val))
