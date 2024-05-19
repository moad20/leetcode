class Solution(object):
    def numberOfSteps(self, num):
        s = 0
        while num > 0:
            if num % 2 == 0:
                num = num / 2
                s = s + 1
            elif num % 2 == 1:
                num = num - 1
                s = s + 1
        return s