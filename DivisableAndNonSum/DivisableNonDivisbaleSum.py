class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # Calculate the sum of all numbers from 1 to n
        total_sum = n * (n + 1) // 2
        
        # Calculate the sum of all numbers from 1 to m
        divisible_sum = m * (n // m) * (n // m + 1) // 2

        # Calculate the sum of all numbers from 1 to n that are not divisible by m
        non_divisible_sum = total_sum - divisible_sum
        
        # Return the difference between the two sums
        return non_divisible_sum - divisible_sum
        

if __name__ == "__main__":
    sol = Solution()
    print(sol.differenceOfSums(10, 3)) # Expected output: 19