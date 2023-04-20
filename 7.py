x = 123
x1 = -123
x3 = 120
x4 = 1563847412
def reverse(x):
    if x < 0:
        s = (str(x)[1:])[::-1]
        temp = '-'+str(s)
    else:
        temp = str(x)[::-1]
    print(int(temp).bit_length())
    print(temp)

print(reverse(x4))