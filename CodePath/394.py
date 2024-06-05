"""
Problem: 
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string
inside the square brackets is being repeated exactly k times. 
Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].
"""
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range (len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                curr = ""
                while stack[-1] != '[':
                    curr = stack.pop() + curr
                # pop '['
                stack.pop()
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                    
                stack.append(int(num) * curr)
        return "".join(stack)