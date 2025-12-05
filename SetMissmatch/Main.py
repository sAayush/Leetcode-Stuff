from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # nums.sort()
        # ans = [0, 0]
        # n = len(nums)

        # for i in range(n - 1):
        #     if nums[i] == nums[i + 1]:
        #         ans[0] = nums[i]
        #     elif nums[i] + 1 != nums[i + 1]:
        #         ans[1] = nums[i] + 1

        # if ans[1] == 0:
        #     if nums[0] != 1:
        #         ans[1] = 1
        #     else:
        #         ans[1] = n

        # return ans

        n = len(nums)
        ex_sum = n * (n + 1) // 2
        ac_sum = sum(nums)

        dupe = 0
        seen = set()
        for i in nums:
            if i in seen:
                dupe = i
                break
            seen.add(i)
        
        missing = ex_sum - (ac_sum - dupe)

        return [dupe, missing]  


if __name__ == "__main__":
    s = Solution()
    print(s.findErrorNums([1,2,2,4]))  # [2,3]
    print(s.findErrorNums([1,1]))      # [1,2]