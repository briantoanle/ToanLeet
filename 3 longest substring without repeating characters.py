s = "abcabcbb"
s1 = "dvdf"
s2 = "pwwke"
# return length of substring without repeating character

def longestSubstring(string):
    left, right = 0, 0

    dictStr = {}
    max = 0
    while right < len(string):
        if string[right] not in dictStr:
            dictStr[string[right]] = 1
        else:
            left += 1
            if dictStr[string[left]] >=1:
                dictStr[string[left]] -= 1
        right += 1
        print('left',left,'right',right)
        print(dictStr)
    return max

def longestSubstringv2(s):
    left = 0
    right = 0

    while right < len(s):

print(longestSubstring(s1))