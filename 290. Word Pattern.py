class Solution(object):
    def wordPattern(self, pattern, s):
        s1 = s.split(" ")
        if len(pattern) != len(s1):
            return False
        d = {}
        for i in range(len(pattern)):
            try:
                if ((pattern[i] in d) or (s1[i] in d.values())) and (d[pattern[i]] != s1[i]):
                    return False
            except KeyError:
                return False
            if s1[i] not in d.values():
                d[pattern[i]] = s1[i]
        return True