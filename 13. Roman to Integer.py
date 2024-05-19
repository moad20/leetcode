class Solution(object):
    def romanToInt(self, s):
        
        self = 0
        for i in range(0,len(s)-1):
            if s[i] == I:
                self = self + 1
            elif s[i] == V:
                self = self + 5
            elif s[i] == X:
                self = self + 10
            elif s[i] == L:
                self = self + 50
            elif s[i] == C:
                self = self + 100
            elif s[i] == D:
                self = self + 500
            else:
                self = self + 1000
        return self