from typing import List

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        for i in range(1,n+1):
            if i in target:
                ans.append("Push")
            else:
                ans.append("Push")
                ans.append("Pop")
            if ans.count("Push") - ans.count("Pop") == len(target):
                break
        
        return ans
    
        # output = []
        # stack = []
        # current_target = target[0]
        # target_index = 0


        # for i in range(1,n+1): # i is index from 1 to n. but target has smaller indices potentially
        # #so how to update target?
        #     if i==current_target:
        #         output.append('Push')
        #         stack.append(i)
        #         if stack==target:
        #             return output
        #         target_index+=1
        #         current_target = target[target_index]
        #     elif i!=current_target:
        #         output.append('Push')
        #         output.append('Pop')
    

if __name__ == "__main__":
    solution = Solution()
    target = [1,3]
    n = 3
    result = solution.buildArray(target, n)
    print(f"Operations to build the target array {target} from 1 to {n} are: {result}")