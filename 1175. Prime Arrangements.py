class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        l = []
        for i in range(2,n+1):
            count = 0
            for j in range(len(l)):
                if i%l[j]==0:
                    count+=1
                    break
            if count==0:
                l.append(i)
        a = len(l)
        b = n  - len(l)
        count = 1
        count1 = 1
        for i in range(1,a+1):
            count*=i
        for j in range(1,b+1):
            count1*=j
        return (count*count1)%((10**9) + 7)


        