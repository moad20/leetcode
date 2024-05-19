class Solution:
    def countAsterisks(self, s):
        count = 0
        ans = 0

        for i in range(len(s)):
            if s[i] == "|":
                count += 1
            if count % 2 == 0:
                if s[i] == "*":
                    ans += 1
        
        return ans
        