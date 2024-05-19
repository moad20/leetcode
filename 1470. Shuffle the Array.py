class Solution(object):
    def shuffle(self, nums, n):
        c1 = []
        c2 = []
        c3 = []
        for i in range(n):
            c1.append(nums[i])
        for i in range(n,2*n):
            c2.append(nums[i])
        for i in range(n):
            c3.append(c1[i])
            c3.append(c2[i])
        return c3