from typing import List


# class Solution:
#     def shuffle(self, nums: List[int], n: int) -> List[int]:
#         ans = []
#         curr = n
#         for i in range(n):
#             ans.append(nums[i])
#             ans.append(nums[curr])
#             curr += 1
#         return ans


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        z=[]
        for i in range(0,n):
            z.append(nums[i])
            z.append(nums[n+i])
        return z
    
if __name__ == "__main__":
    s = Solution()
    print(s.shuffle([2,5,1,3,4,7], 3))  # [2,3,5,4,1,7]
    print(s.shuffle([1,2,3,4,4,3,2,1], 4))  # [1,4,2,3,3,2,4,1]
    print(s.shuffle([1,1,2,2], 2))  # [1,2,1,2]