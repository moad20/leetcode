class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:

        return sorted(
            [[r, c] for r in range(0, rows, 1) for c in range(0, cols, 1)],
            key=lambda coord: abs(coord[0] - rCenter) + abs(coord[1] - cCenter),
        )