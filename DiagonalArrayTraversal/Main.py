from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        rows, cols = len(mat), len(mat[0])
        result = []
        row, col = 0, 0
        upward = True

        while row < rows and col < cols:
            result.append(mat[row][col])
            if upward:
                if col == cols - 1:
                    row += 1
                    upward = False
                elif row == 0:
                    col += 1
                    upward = False
                else:
                    row -= 1
                    col += 1
            else:
                if row == rows - 1:
                    col += 1
                    upward = True
                elif col == 0:
                    row += 1
                    upward = True
                else:
                    row += 1
                    col -= 1

        return result
    

if __name__ == "__main__":
    sol = Solution()
    mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(sol.findDiagonalOrder(mat))  # Output: [1,2,4,7,5,3,6,8,9]    