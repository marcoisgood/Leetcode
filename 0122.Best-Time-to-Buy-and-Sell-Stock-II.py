'''Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit.
You may complete as many transactions as you like
(i.e., buy one and sell one share of the stock multiple times).
Note: You may not engage in multiple transactions at the same time
(i.e., you must sell the stock before you buy again).'''

class Solution:
    def maxProfit(self, prices):
        max = 0;
        for i in range(1,len(prices)):
            p = prices[i]-prices[i-1]
            if p > 0:
                max = max + p
        return max

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]#ans: 7 #[1,2,3,4,5] ans:4
    result = Solution().maxProfit(prices)
    print(result)
