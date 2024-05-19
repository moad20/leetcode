class Solution(object):
    def missingNumber(self, nums):
        num_dict = {}
        for i in nums:
            if i not in num_dict:
                num_dict[i] = 1
                
        for j in range(len(nums)+1):
            if j not in num_dict:
                return j