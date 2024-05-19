class Solution(object):
    def smallestRangeI(self, nums, k):
        max1 = max(nums)
        min1 = min(nums)
        d = max1 - min1
        if d <= 2*k:
            return 0
        else:
            return d - 2*k 