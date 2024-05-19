class Solution:
    def smallerNumbersThanCurrent(self, nums):
        num = sorted(nums)
        return [num.index(i) for i in nums]