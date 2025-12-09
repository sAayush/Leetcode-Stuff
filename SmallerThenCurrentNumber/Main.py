from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        size = len(nums)
        for num in nums:
            count = 0
            for i in range(size):
                if num > nums[i]:
                    count += 1
            ans.append(count)
        return ans
    
if __name__ == "__main__":
    s = Solution()
    print(s.smallerNumbersThanCurrent([8,1,2,2,3]))  # [4,0,1,1,3]
    print(s.smallerNumbersThanCurrent([6,5,4,8]))    # [2,1,0,3]
    print(s.smallerNumbersThanCurrent([7,7,7,7]))    # [0,0,0,0]