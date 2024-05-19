class Solution(object):
    def addDigits(self, num):
        def isFinish(n):
            m = 0
            while n != 0:
                r = n % 10
                m += r
                n = n / 10
            if m/10 == 0:
                return m
            else:
                return isFinish(m)
        return isFinish(num)