from typing import List

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        if not mat or not mat[0]:
            return 0

        rows, cols = len(mat), len(mat[0])
        dp = [[0] * cols for _ in range(rows)]
        count = 0

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 1:
                    # how this works is by using dynamic programming to keep track of the height of 1s
                    # and then for each 1, we extend the rectangle as far left as we can
                    dp[i][j] = dp[i - 1][j] + 1 if i > 0 else 1
                    # we then find the minimum width of the rectangle
                    width = dp[i][j]
                    # we then count all rectangles that can be formed with the bottom-right corner at (i, j)
                    for k in range(j, -1, -1):
                        if dp[i][k] == 0:
                            break
                        width = min(width, dp[i][k])
                        count += width

        return count

if __name__ == "__main__":
    solution = Solution()
    mat = [[1,0,1],[1,1,0],[1,1,0]]
    print(solution.numSubmat(mat))  # Output: 13