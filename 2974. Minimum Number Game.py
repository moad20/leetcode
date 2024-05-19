class Solution(object):
    def numberGame(self, nums):
        res = []
        nums.sort()
        while len(nums) :
            a = nums.pop(0)
            b = nums.pop(0)
            res.append(b)
            res.append(a)
        return res