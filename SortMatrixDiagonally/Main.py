from typing import List

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        diagonals = {}

        # Extract all diagonals
        for i in range(n):
            for j in range(n):
                key = i - j
                if key not in diagonals:
                    diagonals[key] = []
                diagonals[key].append(grid[i][j])

        # Sort each diagonal according to its position
        for key in diagonals:
            if key >= 0:  # bottom-left triangle (including main diagonal)
                diagonals[key].sort(reverse=True)
            else:         # top-right triangle
                diagonals[key].sort()

        # Reconstruct the matrix
        result = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                key = i - j
                result[i][j] = diagonals[key].pop(0)

        return result


if __name__ == "__main__":
    sol = Solution()
    matrix = [[1,7,3],[9,8,2],[4,5,6]]
    sorted_matrix = sol.sortMatrix(matrix)
    for row in sorted_matrix:
        print(row)
