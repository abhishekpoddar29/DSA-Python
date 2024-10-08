'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
'''
def max_profit(prices):
    '''
    min_price=float('inf')
    max_profit=0
    for i in prices:
        if i<min_price:
            min_price=i
        elif i-min_price>max_profit:
            max_profit=i-min_price
    return max_profit
    '''
    l,r=0,1
    profit=0
    while r!=len(prices):
        if prices[l]<prices[r]:
            cur_profit=prices[r]-prices[l]
            profit=max(profit,cur_profit)
        else:
            l=r
        r+=1
    return profit

prices_input = input("Enter numbers for prices separated by spaces: ")
prices = list(map(int, prices_input.split()))
print(max_profit(prices))