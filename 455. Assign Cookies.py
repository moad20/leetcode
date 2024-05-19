class Solution(object):
    def findContentChildren(self, g, s):
        if len(g) == 0 or len(s) == 0:
            return 0
    
        res = 0
        g, s = sorted(g), sorted(s)
        while s and g:
            cookie = s.pop()
            while g:
                greed = g.pop()
                if greed <= cookie:
                    res += 1
                    break
    
        return res