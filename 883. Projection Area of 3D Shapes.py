class Solution:
    def projectionArea(self, arr):
        res = 0
        c = 0

        for i in range(len(arr)):
            res1 = -1
            res2 = -1

            for j in range(len(arr)):
                if arr[i][j] == 0:
                    c += 1
                res1 = max(res1, arr[i][j])
                res2 = max(res2, arr[j][i])

            res += res1 + res2

        return res + len(arr) * len(arr) - c