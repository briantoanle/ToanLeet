'''
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''
n1 = [2,7,11,15]
t1 = 9
n2 = [3,2,4]
t2 = 6

def twoSum(nums,target):
    print(nums)
    print(target)
    temp = []
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if nums[i]+nums[j] == target:
                return [i,j]
print(twoSum(n1,t1))


'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
'''