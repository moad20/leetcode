class Solution:
    def restoreString(self, s, indices):
        a=""
        indices=list(indices)
        for i in range(len(s)):
            b=indices.index(i)
            a+=s[b]
        return a