class Solution(object):
    def xorOperation(self, n, start):
        res = 0
        for i in range(n):
            res ^= start + 2 * i
        return res