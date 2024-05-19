class Solution(object):
    def numberOfMatches(self, n):
        match = 0
        while n > 1:
            if n % 2 == 0:
                match = match + (n//2)
                n = n // 2
            else:
                match = match + (n-1)//2
                n = ((n-1) // 2) + 1
        return match
        