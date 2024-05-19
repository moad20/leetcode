class Solution(object):
    def reverseOnlyLetters(self, s):
        res = ""
        def findalpha(reverseidx) : 
            while reverseidx > 0 and not s[reverseidx].isalpha() : 
                reverseidx-=1
            return reverseidx
        reverseidx = findalpha(len(s)-1)
        for char in s : 
            if char.isalpha() : 
                res += s[reverseidx]
                reverseidx = findalpha(reverseidx-1)
            else : 
                res += char
        return res