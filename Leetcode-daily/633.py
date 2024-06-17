"""
Problem:
Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.
"""
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(sqrt(c)) + 1
        while left <= right:
            goal = left * left + right * right
            if goal == c:
                return True
            elif goal > c:
                right -=1
            else:
                left +=1
        return False
        
        