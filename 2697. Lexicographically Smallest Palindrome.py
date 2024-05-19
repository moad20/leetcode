class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        
        array = list(s)

        i, j = 0 , len(array)-1

        if len(array) == 1:
            return ''.join(array)

        while i < j:
            if array[i]!= array[j]:
                if ord(array[i])<ord(array[j]):
                    array[j] = array[i]
                else:
                    array[i] = array[j]
            if array == array[::-1]:
                return "".join(array)
            i = i+1
            j = j-1
        