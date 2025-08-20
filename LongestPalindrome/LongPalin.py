class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = {}
        for word in words:
            count[word] = count.get(word, 0) + 1
        
        length = 0
        odd_center = False
        
        for word, cnt in count.items():
            if word[0] == word[1]:
                # For words like "aa", "bb", we can use pairs
                length += (cnt // 2) * 4 # Each pair contributes 4 to the length
                if cnt % 2 == 1:
                    odd_center = True
                    
            else:
                # For words like "ab", "ba", we can use pairs
                reverse_word = word[::-1]
                if reverse_word in count:
                    pairs = min(cnt, count[reverse_word])
                    length += pairs * 4
                    count[reverse_word] = 0
                    count[word] = 0
                    
        # If we have an odd center, we can add 2 to the length
        if odd_center:
            length += 2
        return length
    

if __name__ == "__main__":
    from typing import List
    words = ["ab", "ba", "aa", "bb"]
    sol = Solution()
    print(sol.longestPalindrome(words))  # Expected output: 8