class Solution:
    def fairCandySwap(self, a: List[int], b: List[int]) -> List[int]:
       s=sum(a)
       r=sum(b)
       if s>r:
            b=set(b)
            for i in range(len(a)):
                if (r-s+2*a[i])//2 in b:
                    return [a[i],(r-s+2*a[i])//2 ]
       else:
            a=set(a)
            print(a,r,s,b)
            for i in range(len(b)):
                if (s-r+2*b[i])//2 in a:
                    return [(s-r+2*b[i])//2,b[i]]