from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        count = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    dp[i][j] = 1
                    if i > 0 and j > 0:
                        # How this works is - we are looking for the smallest square that can be formed
                        # by taking the minimum of the three neighboring squares
                        dp[i][j] += min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                    # in here we are adding 1 to account for the current cell
                    count += dp[i][j]

        return count
    
if __name__ == "__main__":
    solution = Solution()
    matrix = [
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 1, 1, 1]
    ]
    print(solution.countSquares(matrix))