class Solution:
    def maxWidthOfVerticalArea(self, points):
        a=[]
        for i in points:
            a.append(i[0])
        a.sort()
        maxwidth=a[1]-a[0]
        for i in range(2,len(a)-1):
            if maxwidth<a[i+1]-a[i]:
                maxwidth=a[i+1]-a[i]
        return maxwidth


                    