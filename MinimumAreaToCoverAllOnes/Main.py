from typing import List

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        min_row, min_col = float('inf'), float('inf')
        max_row, max_col = float('-inf'), float('-inf')

        # Here we find the min and max row/col that contains 1
        for r in range(len(grid)):
            # Iterate through each row index 'r'
            for c in range(len(grid[0])):
                # Iterate through each column index 'c' in the current row
                # If we find a 1, we update our min/max bounds
                if grid[r][c] == 1:
                    # Update the minimum row index where a 1 is found
                    min_row = min(min_row, r)
                    # Update the minimum column index where a 1 is found
                    min_col = min(min_col, c)
                    # Update the maximum row index where a 1 is found
                    max_row = max(max_row, r)
                    # Update the maximum column index where a 1 is found
                    max_col = max(max_col, c)
        # Here we check if we found any 1s, if not we return 0
        if min_row == float('inf'):
            # If no 1s were found, return 0 as the area
            return 0

        # Calculate the area of the rectangle formed by the min/max row/col
        return (max_row - min_row + 1) * (max_col - min_col + 1)

if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumArea([[0,0,0],[0,1,1],[0,1,1]]))  # Output: 4