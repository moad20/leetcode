class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        count = 0
        for i in stones:
            if i in jewels:
                count += 1 
        return count
        return len([i for i in stones if i in jewels])
        return sum([stones.count(i) for i in jewels])
        return sum([i in jewels for i in stones])