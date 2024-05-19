class Solution(object):
    def plusOne(self, digits):
        num_string_list = list(map(str, digits))
        num_string = ''.join(num_string_list)
        my_number = int(num_string) + 1
        answer_number_string = list(str(my_number))
        
        answer = list(map(int, answer_number_string))
        return answer