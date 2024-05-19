class Solution:
    def sortString(self, s: str) -> str:
        # initialise a list of lowercase alphabets
        lowercase_alphabets = [chr(i) for i in range(97, 123)]

        # initialise an empty dict 'letter_to_occ' to store letters and their occurences
        letter_to_occ = {}

        # loop through the string 's' and map letters to their occurences
        for letter in s:
            letter_to_occ[letter] = letter_to_occ.get(letter, 0) + 1
        
        # initialise an empty string 'ans' to store the answer
        ans = ''

        # loop until all the occurences in letter_to_occ become '0'
        while not all(values==0 for values in letter_to_occ.values()):
            # loop through the lowercase_alphabets
            for letter in lowercase_alphabets:
                # check if the letter exists in 'letter_to_occ' and that letter's occurence is != 0
                if letter in letter_to_occ and letter_to_occ[letter] != 0:
                    # add the letter into the 'ans'
                    ans += letter
                    # decrement the occurence of the current letter by 1
                    letter_to_occ[letter] -= 1
            
            # reverse the list
            lowercase_alphabets = lowercase_alphabets[::-1]
        
        return ans
