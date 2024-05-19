class Solution(object):
    def subtractProductAndSum(self, n):
        pro = 1
        sum = 0
        for i in str(n):
            pro = pro*(int(i))
            sum = sum + (int(i))
        return pro - sum