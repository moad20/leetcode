class Solution(object):
    def singleNumber(self, nums):
        s = set()
        for i in nums:
            if i not in s: 
                s.add(i)
            else:
                s.remove(i)
        return list(s)[0]