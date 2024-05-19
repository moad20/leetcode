class Solution(object):
    def getConcatenation(self, nums):
        ans = []
        for i in nums:
            ans.append(i)
        ans = ans + nums
        return ans