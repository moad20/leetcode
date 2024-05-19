class Solution(object):
    def decode(self, encoded, first):
        n = len(encoded)
        arr1 = [0]*(n+1)
        arr1[0] = first
        for i in range(1,n+1):
            arr1[i] = encoded[i-1]^arr1[i-1]
        return arr1