class Solution(object):
    def differenceOfSums(self, n, m):
        s = 0
        s1 = 0
        for i in range(1,n+1):
            if i % m == 0:
                s = s + i
            elif i % m != 0:
                s1 = s1 + i
        return s1 - s