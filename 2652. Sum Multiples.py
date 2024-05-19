class Solution(object):
    def sumOfMultiples(self, n):
        a = 0
        for i in range(0,n+1):
            if (i % 3 == 0) or (i % 5 == 0) or (i % 7 == 0):
                a = a + i
        return a