class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        # nasty one liner
        return [[(sum([img[r+y][c+x] for y, x in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1), (0, 0)] if 0 <= r+y < len(img) and 0 <= c + x < len(img[0])]) 
               // len([img[r+y][c+x] for y, x in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1), (0, 0)] if 0 <= r+y < len(img) and 0 <= c + x < len(img[0])])) 
            for c in range(len(img[0]))] 
            for r in range(len(img))]

        # Actual Solution in O(m*n) time, O(m*n) space
        #  call dfs on each of the cells to get the average 
        rows = len(img)
        cols = len(img[0])
        # initialize smoothed image
        smoothedImg = [[0 for y in range(cols)] for x in range(rows)]
        # 8 directions 
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1), (0, 0)]

        # iterate through the whole img calling dfs and adding the average to a new matrix
        for r in range(rows): 
            for c in range(cols): 
                avg = []
                for y, x in dirs: 
                    # append dirs
                    ry = r + y
                    cx = c + x
                    if 0 <= ry < len(img) and 0 <= cx < len(img[0]): 
                        avg.append(img[ry][cx])
                smoothedImg[r][c] = sum(avg)//len(avg)  
        
        return smoothedImg