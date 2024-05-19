class Solution:
    def groupThePeople(self, groupSizes):
        dic = {}
        for person, groupsize in enumerate(groupSizes):
            dic[groupsize] = dic.get(groupsize, []) + [person]      
        return [lst[i:i+key] for key, lst in dic.items() for i in range(0,len(lst),key)]