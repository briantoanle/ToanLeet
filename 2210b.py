"""
Consider the problem of finding missing numbers in an integer array which contains duplicates.
The array may contain more than one duplicate values. For the purpose of this exercise you can
consider that the array will contain the range of values starting at 0 that would be enough to cover
the size of the array. As an example consider the array L with length(L) = 5. L = [0,1,1,2,3]. The
missing number would be 4 because we work under the assumption that L is an array containing all
numbers in [0, len(L)-1] where len(L) is the length of the array, and the square brackets show
inclusion of the edge values.

"""

l = [0,1,1,2,3]
#     0,1,2,3,4,5,6,7,8,9
l1 = [0,8,4,3,2,5,6,7,8,2]
# missing 9, 1
# Time complexity is: O(2n) --> O(n)



# 0,1,2,3,4
# 0,1,1,2,3

# if
def findMissingNumber(l):
    count = 0
    f = []
    for i in range(len(l)):
        f.append(i)
    l = set(l)
    print(l)
    for i in l:
        f.remove(i)
    print(f)


def find(l):
    result = []
    f = [0] * len(l)
    print(f)
    for i in range(len(l)):
        f[l[i]] += 1
    for i in range(len(f)):
        if f[i] == 0:
            result.append(i)

    print(f)
    return result


print(find(l1))
