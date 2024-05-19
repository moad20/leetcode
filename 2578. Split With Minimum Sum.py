class Solution(object):
    def splitNum(self, num):
        sorted_str = "".join(sorted([i for i in str(num)]))
        num1,num2 = "", ""
        for i in range(len(sorted_str)):
            if i%2 == 0:
                num1 += sorted_str[i]
            else:
                num2 += sorted_str[i]
        return int(num1)+int(num2)