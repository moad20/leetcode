class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        a = []
        for i in range(len(hours)):
            if hours[i] >= target:
                a.append(hours[i])
        return len(a)