class Solution(object):
    def isPalindrome(self, x):
        pro = None
        if x < 0:
            pro = False
        else:
            original = x
            reverse = 0
            while x:
                remainder = x % 10
                x = x // 10
                reverse = reverse*10 + remainder

            if reverse == original:            
                pro = True
            else:
                pro = False
        
        return pro