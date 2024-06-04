"""
Problem: 
Given a string s which consists of lowercase or uppercase letters, return the length of the longest 
palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome.
"""
class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s)
        ans = 0
        has_odd = False
        for char, freq in cnt.items():
            if freq % 2 == 0:
                ans += freq
            else:
                ans += freq - 1
                has_odd = True
        if has_odd:
            ans +=1
        return ans
        