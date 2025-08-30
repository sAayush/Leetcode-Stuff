from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid_block(block: List[str]) -> bool:
            seen = set()
            for num in block:
                if num != ".":
                    if num in seen:
                        return False
                    seen.add(num)
            return True

        # Check rows
        for row in board:
            if not is_valid_block(row):
                return False

        # Check columns
        for col in range(9):
            if not is_valid_block([board[row][col] for row in range(9)]):
                return False

        # Check 3x3 sub-boxes
        for box_row in range(3):
            for box_col in range(3):
                if not is_valid_block([board[row][col]
                                        for row in range(box_row * 3, (box_row + 1) * 3)
                                        for col in range(box_col * 3, (box_col + 1) * 3)]):
                    return False

        return True


if __name__ == "__main__":
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]]
    solution = Solution()
    print(solution.isValidSudoku(board))