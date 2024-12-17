class Solution:
    def checkSides(self,grid,i,j,m,n):
        p=0
        if(i==0 or grid[i-1][j]==0):
            p+=1
        if(i==m or grid[i+1][j]==0):
            p+=1
        if(j==0 or grid[i][j-1]==0):
            p+=1
        if(j==n or grid[i][j+1]==0):
            p+=1
        return p

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        perimeter=0
        for i in range(m):
            for j in range(n):
                if(grid[i][j]==1):
                    perimeter+=self.checkSides(grid,i,j,m-1,n-1)
        return perimeter