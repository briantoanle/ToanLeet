'''
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

'''

haystack = 'sadbutsad'
needle = 'sad'
haystack = "leetcode"
needle = "leeto"
haystack = 'hello'
needle = 'll'
haystack = 'abc'
needle = 'c'
def find(haystack, needle):
    print(haystack,needle)
    for i in range(len(haystack)):
        print(haystack[i])
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1

print(find(haystack,needle))