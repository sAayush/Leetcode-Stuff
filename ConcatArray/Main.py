from ast import List
import numpy as np

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # nums.extend(nums)
        # nums = nums + nums
        nums = np.concatenate((nums, nums)).tolist()
        return nums
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.getConcatenation([1,2,3]))