from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        total = 0
        for num in nums:
            if num == 0:
                count += 1
                total += count
            else:
                count = 0
        return total

if __name__ == "__main__":
    sol = Solution()
    print(sol.zeroFilledSubarray([1, 0, 0, 2, 0, 0, 0, 3]))