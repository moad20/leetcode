class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n==1 if n<=1 else int(sqrt(n)) * int(sqrt(n)) == n and int(sqrt(n)).bit_count() == 1