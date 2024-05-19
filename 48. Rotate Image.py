class Solution(object):
    def rotate(self, matrix):
        n = []
        for row in matrix:
            n.append(row[:])
        for x in range(len(matrix)):
            for y in range(len(matrix)):
                matrix[x][y] = n[len(matrix)-y-1][x]
        print(n)
        matrix = n