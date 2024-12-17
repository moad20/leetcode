class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        # If the source cell already has the same value as `color`, return the 
        # original image
        if image[sr][sc] == color:
            return image

        # Storing the original value of the starting cell
        old_color = image[sr][sc]
        # Replacing the value of the starting cell with the specified color
        image[sr][sc] = color

        # Calling the dfs function to replace the values of all connected cells
        self.dfs(image, sr, sc, old_color, color)

        # Return the modified image
        return image

    def dfs(
        self,
        grid: List[List[int]],
        row: int,
        col: int,
        old_target: int,
        new_target: int,
    ):
        # Defining the four cells adjacent to the starting cell
        adjacent_cells = [
            [0, 1],  # move right
            [1, 0],  # move down
            [-1, 0],  # move up
            [0, -1],  # move left
        ]

        # Get the dimensions of the grid
        grid_length = len(grid)
        total_cells = len(grid[0])

        # For each cell in the list of adjacent cells
        for cell_value in adjacent_cells:
            r = row + cell_value[0]
            c = col + cell_value[1]

            # If the adjacent cell is within the bounds of the grid
            # and has the same value as the starting cell
            if (
                0 <= r < grid_length
                and 0 <= c < total_cells
                and grid[r][c] == old_target
            ):
                # Replace the value of the adjacent cell with the specified 
                # target
                grid[r][c] = new_target
                # Recursively call the dfs function on the adjacent cell
                self.dfs(grid, r, c, old_target, new_target)