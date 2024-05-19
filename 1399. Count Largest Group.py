class Solution(object):
    def countLargestGroup(self, n):
        def ds(n):
            s=0
            for i in str(n):
                s=s+int(i)
            return s
        d={}
        if (n<=9):
            return n
        else:
            m=0
            c=0
            for i in range(10,n+1):
                s=ds(i)
                if (s in d):
                    d[s]+=1
                else:
                    if (s<10):
                        d[s]=2
                    else:
                        d[s]=1
                # print(d)
                if (d[s]>m):
                    m=d[s]
            for i in d.keys():
                if(d[i]==m):
                    # print(d[i])
                    c+=1
            return c