class Solution(object):
    def finalValueAfterOperations(self, operations):
        result = 0
        for i in range(len(operations)):
            if(operations[i] == '++X' or operations[i] == 'X++'):
                result = result + 1
            else:
                result = result - 1
        return result