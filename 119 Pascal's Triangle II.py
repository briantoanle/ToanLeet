

# given index of row, return an array

def pascalTriangle(index):
    if index == 0:
        return [1]
    else:
        arr = [1,1]

        for i in range(2,index+1):
            temp = []
            temp.append(1)
            for j in range(0,i-1):
                temp.append(arr[j] + arr[j+1])
            temp.append(1)
            arr = temp
        return arr

print(pascalTriangle(6))
