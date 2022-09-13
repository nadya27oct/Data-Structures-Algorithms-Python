"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the
future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
Example1:
Input: prices = [7,1,5,3,6,4]
Output: 5

Example2:
Input: prices = [2,4,1]
Output: 2

Example3:
Input: prices = [7,6,4,3,1]
Output: 0

Example4:
Input: prices = [7,6,4,3,10,1,43]
Output: 40
{3: 1, 4: 43, 5: 3, 6: 10}


"""

class Solution:
    def maxProfit(self, prices):

        total_days = len(prices)

        if total_days <= 1:
            return 0

        buy_price = 0
        profit = 0
        for i in range(total_days-1):
            if prices[i+1] > prices[i]:
                if buy_price == 0 and profit ==0:
                    buy_price = prices[i]
                if prices[i] < buy_price:
                    buy_price = prices[i]

                if prices[i+1] - buy_price > profit:
                    profit = prices[i+1] - buy_price

        return profit

obj = Solution()
example1 = obj.maxProfit([7,6,4,3,10,6,40])
print(example1)
example2 = obj.maxProfit([2,5,1])
print(example2)
prices = [886,729,539,474,5,653,588,198,313,111,38,1808,848,364,819,747,520,568,583,253,605,442,779,903,217,284,927,33,859,75,418,612,174,316,167,40,945,740,174,279,985,133,38,919,528,844,101,291,673,561,244,827,602,58]
example3 = obj.maxProfit(prices)
print(example3)
example4 = obj.maxProfit([2,1,2,1,0,1,2])
print(example4)
