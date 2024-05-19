class Solution:
    def maximizeSum(self, nums, k):
        max_num = max(nums)
        total = 0

        for n in range(max_num, max_num + k):
            total += n

        return total