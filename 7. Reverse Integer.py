class Solution(object):
    def reverse(self, x):
        if x == 0 :
            return 0
        while not x % 10 :
            x //= 10
        sx = str(abs(x))
        l = len(sx)
        res = 0
        for i in range(l) :
            res += 10**i * int(sx[i])
        if res.bit_length() > 31 :
            return 0
        if x >= 0 :
            return res
        return -res