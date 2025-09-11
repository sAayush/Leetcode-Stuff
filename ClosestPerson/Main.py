class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        if abs(x - z) < abs(y - z):
            return 1
        elif abs(x - z) > abs(y - z):
            return 2
        else:
            return 0
    
if __name__ == "__main__":
    x, y, z = 2, 7, 4
    solution = Solution()
    print(solution.findClosest(x, y, z))