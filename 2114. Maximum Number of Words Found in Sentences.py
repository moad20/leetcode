class Solution(object):
    def mostWordsFound(self, sentences):
        m = 0
        for i in sentences:
            c = 0
            for j in i:
                if j == ' ':
                    c = c + 1
            m = max(m, c+1)
        return m