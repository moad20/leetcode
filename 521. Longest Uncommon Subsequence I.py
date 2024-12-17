class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a==b :
            return -1
        else:
            # Return the length of the longer string
            return max(len(a), len(b))