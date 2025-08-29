class Solution:
    def flowerGame(self, n: int, m: int) -> int:
         return (m * n) // 2

if __name__ == "__main__":
    sol = Solution()
    print(sol.flowerGame(3, 2))