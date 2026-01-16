from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            # print("i :", i)
            if i not in ['+', '-', '*', '/']:
                stack.append(int(i))
                # print("stack: ", stack)
            else:
                b = stack.pop()
                a = stack.pop() 
                stack.append(int(eval(f"{a}{i}{b}")))
                # print("stack: ", stack)
        return stack[0]
    
        # stack = []
        # for i in tokens:
        #     # print("i :", i)
        #     if i not in ['+', '-', '*', '/']:
        #         stack.append(int(i))
        #         # print("stack: ", stack)
        #     else:
        #         right = stack.pop()
        #         left = stack.pop()

        #         if i == "+":
        #             stack.append(left + right)
        #         elif i == "-":
        #             stack.append(left - right)
        #         elif i == "*":
        #             stack.append(left * right)
        #         elif i == "/":
        #             stack.append(int(left / right))

        # return stack[0]


if __name__ == "__main__":
    sol = Solution()
    tokens = ["2", "1", "+", "3", "*"]
    print(sol.evalRPN(tokens))  # Output: 9

    tokens = ["4", "13", "5", "/", "+"]
    print(sol.evalRPN(tokens))  # Output: 6