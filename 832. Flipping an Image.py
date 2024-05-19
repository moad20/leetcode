class Solution:
    def flipAndInvertImage(self, image):
        return  [[e ^ 1 for e in row[::-1]] for row in image]