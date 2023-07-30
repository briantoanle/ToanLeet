"""
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achive this answer too.
"""




def characterReplacement(s,k) -> int:
    left, right, final = 0, 0, 0

    while right < len(s):
        print(s[right])
        print("substring =", s[left:right+1])
        if cR(s[left:right+1], k):
            print("Trigger TRUE")
            final = right - left + 1
        else:
            left += 1

        right += 1

        print("final so far is:", final)

    return final
    '''
    final = 1 +  k
    left = 0
    print("STRING: ", s, len(s)-final)
    for right in range(1,len(s)-final):
        #print("here", s[right])
        print(s[left:left+final])
        if(cR(s[left:left+final],k)):
            final += 1
        else:
            left += 1

    return final - 1
    '''

def cR(s, k):
    #print("in CR", s)
    if len(s) <= k:
        # print('True',s)
        return True
    dictionary = {}
    for i in s:
        if i not in dictionary:
            dictionary[i] = 1
        else:
            dictionary[i] += 1
    for key,value in dictionary.items():
        if value+k >= len(s):
            # print('True', s)
            return True

    return False
s = 'AABABBACBCCBACCCA'
z = 'ASDHKJHO'
l = 'LAJALKAA'
k = 2
#print(characterReplacement(s,3))

print(cR("BCBBBBB", 2))
