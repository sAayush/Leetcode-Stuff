class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []
        for i, word in enumerate(words):
            if x in word:
                result.append(i)
        return result
    
# class Solution:
#     def findWordsContaining(self, words: List[str], x: str) -> List[int]:
#         a=[]
#         for i in range(len(words)):
#             if x in words[i]:
#                 a.append(i)
#         return a


if __name__ == "__main__":
    words = ["hello", "world", "python", "code"]
    x = "o"
    solution = Solution()
    result = solution.findWordsContaining(words, x)
    print(result)  # Output: [1, 2]