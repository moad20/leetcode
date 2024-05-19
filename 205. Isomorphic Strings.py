class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False

        mapS2T = {}
        mapT2S = {}

        for charS, charT in zip(s, t):
            if charS in mapS2T:
                if mapS2T[charS] != charT:
                    return False
            else:
                if charT in mapT2S:
                    return False

                mapS2T[charS] = charT
                mapT2S[charT] = charS

        return True