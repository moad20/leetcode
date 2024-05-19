class Solution(object):
    def alternateDigitSum(self, n):
        n = str(n)
        sum_, flag = 0, True
        for ch in n:
            sum_ += int(ch) if flag else -int(ch)
            flag = not flag
        return sum_