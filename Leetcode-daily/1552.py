"""
Problem:
In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket. Rick has n empty baskets, the ith basket is at position[i], Morty has m balls and needs to distribute the balls into the baskets such that the minimum magnetic force between any two balls is maximum.

Rick stated that magnetic force between two different balls at positions x and y is |x - y|.

Given the integer array position and the integer m. Return the required force.
"""
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def totalBall(position, force):
            total = 1 
            prev = position[0]
            for i in range (1, len(position)):
                curr = position[i]
                if curr - prev >= force:
                    total +=1
                    prev = curr
            return total 
        position.sort()
        left = 0
        right = position[-1] - position[0]
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if totalBall(position, mid) >= m:
                ans = max(mid, ans)
                left = mid + 1
            else:
                right = mid - 1
        return ans 


        