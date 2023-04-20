'''
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
'''

digits = [1,2,3]
digits1 = [9,9]
digits2 = [1,2,3,4,5,6,7,8,9,9,9]
digits3 = [8,9,9,9]
digits4 = [9,9]
'''def plusOne(digits):
    if digits[-1] < 9:
        digits[-1] = digits[-1]+1
        return digits
    else:
        for i in range(len(digits)-1,0,-1):
            print(i)
            if digits[i] == 9:
                digits[i] = 0
                digits[i-1] = digits[i-1]+1
            if digits[i] == 10:
                digits[i] = 0
                digits[i-1] = digits[i-1]+1
        return digits'''
#print(plusOne(digits4))
def plusOne(digits):
    s = ''
    for i in digits:
        s+=str(i)
    num = int(s)+1
    s = str(num)

    arr = []
    for i in range(len(s)):
        arr.append(int(s[i]))
    return arr
plusOne(digits4)