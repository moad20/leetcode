class Solution(object):
    def isStrictlyPalindromic(self, n):
        for i in range(2, n - 1):
            values = ""
            j = n
            while j != 0:
                r = j % i 
                j = j // i

                values  = str(r) + values
            
            if values != values[::-1]:
                return False
        return True