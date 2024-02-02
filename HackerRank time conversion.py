

def testCase1():
    s = '07:05:45PM'
    output = '19:05:45'
    timeConversion(s)
def testCase2():
    s = '12:45:54PM'
    output = '00:01:55'
    timeConversion(s)
def timeConversion(s):
    AmPm = s[-2::]
    time = ''
    if AmPm == 'PM' and s[0:2] != '12':
        time += str(int(s[0:2]) +12)
    elif s[0:2] == '12' and AmPm == 'AM':
        time += '00'
    else:
        print(s[0:8])
    time += s[2:8]
    print(time)

#testCase1()
testCase2()