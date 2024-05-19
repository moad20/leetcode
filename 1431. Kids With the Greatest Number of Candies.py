class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        maximum =max(candies)
        result=[]
        for i in range(len(candies)):
            total = candies[i] + extraCandies
            result.append(total >= maximum)
        return result