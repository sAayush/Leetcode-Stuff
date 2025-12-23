from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # num_set = set(nums)
        # result = []
        # for i in range(1, n+1):
        #     if i not in num_set:
        #         result.append(i)

        # return result 

        size = len(nums)
        all_nums = []
        for i in range(size):
            all_nums.append(i+1)
        
        missing = list(set(all_nums) - set(nums))
        return missing

if __name__ == "__main__":
    solution = Solution()
    test_nums = [4, 3, 2, 7, 8, 2, 3, 1]
    result = solution.findDisappearedNumbers(test_nums)
    print(f"Disappeared numbers in the array {test_nums} are: {result}")