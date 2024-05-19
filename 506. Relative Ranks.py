class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        # Initialization
        heap = [] # to store score and their indices
        res = ['']*len(score)
        position = 0

        #push each score and index into heap
        for i in range(len(score)):
            heapq.heappush(heap, (-score[i],i))

        #iterate over all the all scores and pop the score with highest value
        while position < len(score):
            index = heapq.heappop(heap)[1]

        #assign ranks based on the order of popping 
            if position == 0:
                res[index] = 'Gold Medal'
            elif position == 1:
                res[index] = 'Silver Medal'
            elif position == 2:
                res[index] = 'Bronze Medal'
            else:
                res[index] = str(position+1)
            position += 1
        
        return res