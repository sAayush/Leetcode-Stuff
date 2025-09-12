class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = set('aeiou')
        vowel_count = sum(1 for char in s if char in vowels)
        if vowel_count >= 1:
            return True
        return False
    
if __name__ == "__main__":
    solution = Solution()
    s = "abaed"
    print(solution.doesAliceWin(s))