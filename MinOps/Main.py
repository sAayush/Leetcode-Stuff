from ast import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        tsum = sum(nums)
        count = 0
        if tsum < k:
            return tsum

        if tsum % k == 0:
            return count
        
        for i in range(tsum, k-1, -1):
            if i % k == 0:
                return count
            count += 1
        
