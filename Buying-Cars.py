class Solution:
    def solve(self, prices, k):
        prices = sorted(prices)
        total = 0
        count = 0
        for i in range(len(prices)):
            if total <= k and (total + prices[i]) <= k:
                total += prices[i]
                count += 1
        return count