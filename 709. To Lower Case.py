class Solution:
    def toLowerCase(self, s):
        lower_case_str = ""
        for char in s:
            ascii_val = ord(char)
            if 65 <= ascii_val <= 90:
                lower_case_str += chr(ascii_val + 32)
            else:
                lower_case_str += char
        return lower_case_str