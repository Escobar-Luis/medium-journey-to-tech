from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Right pointer will be next to left
        l,r= 0, 1
        # Base case will always be 0 if no profit found
        maxP= 0
        # its less than so we never go out of bounds
        while r< len(prices):
            # if my left p less than right meaning profit
            if prices[l] < prices[r]:
                # calculate profit
                profit = prices[r]-prices[l]
                # set profit or keep old one
                maxP= max(maxP, profit)
            # scenario where my right is lower than left
            else:
                # move left pointer to right
                l = r
            # in every case, keep moving the right pointer as to increase the window.
            r+=1
        return maxP