"""
Problem:
You are given a string s and two integers x and y. You can perform two types of operations any number of times.

Remove substring "ab" and gain x points.
For example, when removing "ab" from "cabxbae" it becomes "cxbae".
Remove substring "ba" and gain y points.
For example, when removing "ba" from "cabxbae" it becomes "cabxe".
Return the maximum points you can gain after applying the above operations on s.
"""
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_str(s, target):
            stack = []
            for char in s:
                if char == target[1] and stack and stack[-1] == target[0]:
                    stack.pop()
                else:
                    stack.append(char)
            return "".join(stack)
        
        ans = 0 
        if x > y:
            higher_pair = "ab"
            lower_pair = "ba"
        else:
            higher_pair = "ba"
            lower_pair = "ab"
        first_pass = remove_str(s, higher_pair)
        ans += (len(s) - len(first_pass)) // 2 * max(x, y)
        second = remove_str(first_pass, lower_pair)
        ans += (len(first_pass) - len(second)) // 2 * min(x, y)
        return ans
        