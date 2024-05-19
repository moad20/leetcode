class Solution:
    def countGoodTriplets(self, A: List[int], a: int, b: int, c: int) -> int:
        n = len(A)
        cnt = 0
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if abs(A[i]-A[j]) <= a and abs(A[k]-A[j]) <= b and abs(A[i]-A[k]) <= c:
                        cnt+=1
        return cnt