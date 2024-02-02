

arr = [4,2,1,7,8,1,2,8,1,0]

# max subarray size 3

# keep a max

def findMaxSum(arr,size=3):
    max = sum(arr[0:3])
    print(max)
    for i in range(1,len(arr)-3):
        tempMax = max - arr[i] + arr[i+3]
        print(tempMax)


findMaxSum(arr)
