from ast import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # size = len(nums)
        # curr = 0
        # res = 0
        # for i in range(size):
        #     if nums[i] == 1:
        #         curr += 1
        #     else:
        #         if res <= curr:
        #             res = curr
        #         curr = 0
        # return res if res > curr else curr
        
        
        # curr = 0
        # res = 0
        # for num in nums:
        #     if num == 1:
        #         curr += 1
        #         res = max(res, curr)
        #     else:
        #         curr = 0
        # return res
        
        curr = 0
        res = 0
        for num in nums:
            if num == 1:
                curr += 1
            else:
                res = max(res, curr)
                curr = 0
        return max(res, curr)
    

if __name__ == "__main__":
    s = Solution()
    print(s.findMaxConsecutiveOnes([1,1,0,1,1,1]))  # 3
    print(s.findMaxConsecutiveOnes([1,0,1,1,0,1]))  # 2
    print(s.findMaxConsecutiveOnes([0,0,0,0,0]))     # 0