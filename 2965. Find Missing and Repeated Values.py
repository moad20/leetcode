class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        arr=[element for sublist in grid for element in sublist]
        arr.sort()
        n=[]
        for i in range(len(arr)-1):
            if arr[i]==arr[i+1]:
                n.append(arr[i])
                arr.remove(arr[i])
                break
        arr.append(1000000)
        for i in range(len(arr)):
            if i+1!=arr[i]:
                n.append(i+1)
                break
        return n