class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = bin(x)[2:]
        b = bin(y)[2:]
        if len(a) > len(b):
            b = '0' * (len(a)-len(b)) + b
        elif len(a) < len(b):
            a = '0' * abs((len(a)-len(b))) + a
        count = 0
        for i in range(len(a)):
            if a[i]!=b[i]:
                count = count + 1
        return count