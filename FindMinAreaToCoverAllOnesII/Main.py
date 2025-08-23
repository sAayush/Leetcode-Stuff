from typing import List
# It can use up to 3 Non overlapping rectangles to cover all 1s
class Solution:
    def minimumSum(self, A: List[List[int]]) -> int:
        """
        Calculates the minimum total area of three non-overlapping rectangles
        that cover all the '1's in the grid.
        It checks all possible ways to partition the grid into three rectangles.
        """
        # Initialize the result to infinity. Any valid area sum will be smaller.
        res = float("inf")

        # The grid is rotated 4 times (0, 90, 180, 270 degrees) to cover all
        # possible partition orientations without writing separate logic for each.
        for _ in range(4):
            n, m = len(A), len(A[0]) # Get current dimensions of the (possibly rotated) grid.

            # === Check partitions starting with one horizontal cut ===
            # Iterate through all possible rows 'i' to make the first horizontal cut.
            # This splits the grid into a top part (A[:i]) and a bottom part (A[i:]).
            for i in range(1, n):
                # Calculate the minimum area for the top part (Part 1).
                a1 = self.minimumArea(A[:i])

                # --- Scenario 1: T-shaped cut ---
                # The bottom part (A[i:]) is split by a vertical cut.
                # Iterate through all possible columns 'j' to make the vertical cut.
                for j in range(1, m):
                    # Define the two rectangles in the bottom part.
                    part2 = [row[:j] for row in A[i:]] # Bottom-left part (Part 2)
                    part3 = [row[j:] for row in A[i:]] # Bottom-right part (Part 3)
                    
                    # Calculate their minimum areas.
                    a2 = self.minimumArea(part2)
                    a3 = self.minimumArea(part3)

                    # If all three parts contain at least one '1', update the minimum sum.
                    if a1 > 0 and a2 > 0 and a3 > 0:
                        res = min(res, a1 + a2 + a3)

                # --- Scenario 2: Three horizontal stripes ---
                # The bottom part (A[i:]) is split by another horizontal cut.
                # Iterate through rows 'i2' for the second horizontal cut.
                for i2 in range(i + 1, n):
                    # Define the middle and bottom rectangles.
                    part2 = A[i:i2] # Middle part (Part 2)
                    part3 = A[i2:]  # Bottom part (Part 3)

                    # Calculate their minimum areas.
                    a2 = self.minimumArea(part2)
                    a3 = self.minimumArea(part3)
                    
                    # If all three parts contain at least one '1', update the minimum sum.
                    if a1 > 0 and a2 > 0 and a3 > 0:
                        res = min(res, a1 + a2 + a3)

            # Rotate the grid 90 degrees clockwise for the next iteration.
            # This allows the same logic to check for vertical and other T-shaped partitions.
            A = self.rotate(A)
            
        return res

    def minimumArea(self, A: List[List[int]]) -> int:
        """
        Helper function to find the area of the smallest bounding box
        that contains all the '1's in a given sub-grid.
        """
        # Handle cases with empty grids.
        if not A or not A[0]:
            return 0
        
        n, m = len(A), len(A[0])
        # Initialize bounding box coordinates.
        # top/left are high so any real coordinate will be smaller.
        # bottom/right are low so any real coordinate will be larger.
        left, top, right, bottom = float("inf"), float("inf"), -1, -1

        # Iterate through every cell to find the boundaries of the '1's.
        for i in range(n):
            for j in range(m):
                if A[i][j] == 1:
                    # Update the boundaries of the bounding box.
                    left = min(left, j)
                    top = min(top, i)
                    right = max(right, j)
                    bottom = max(bottom, i)
        
        # If 'right' is still -1, no '1's were found. The area is 0.
        if right == -1:
            return 0
        
        # Calculate the area from the bounding box coordinates.
        # Add 1 because the coordinates are inclusive (e.g., width from col 2 to 4 is 4-2+1=3).
        return (right - left + 1) * (bottom - top + 1)

    def rotate(self, A: List[List[int]]) -> List[List[int]]:
        """
        Helper function to rotate a matrix 90 degrees clockwise.
        """
        n, m = len(A), len(A[0])
        # A list comprehension to perform the rotation.
        # The new rows are formed by taking the columns of the original matrix in reverse row order.
        # For each column 'j' of the old matrix, create a new row by taking elements
        # A[i][j] where 'i' goes from bottom (n-1) to top (0).
        return [[A[i][j] for i in range(n - 1, -1, -1)] for j in range(m)]


if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumSum([[1,0,1],[1,1,1]])) # should equal to 5
