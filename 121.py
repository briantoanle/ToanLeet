'''
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
'''

prices1 = [7,1,5,3,6,4]
prices = [5,4,3,2,1]
def bestday(prices):
    maxProfit = 0
    lowest = prices[0]

    for i in range(1,len(prices)):
        if prices[i] < lowest:
            lowest = prices[i]

        temp = prices[i] - lowest
        if temp > maxProfit:
            maxProfit = temp
    print('max',maxProfit)


bestday(prices1)