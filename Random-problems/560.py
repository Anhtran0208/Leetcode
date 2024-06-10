"""
Problem: (related to 974)
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0: 1}
        ans = 0 
        curr = 0
        for i in range (len(nums)):
            curr += nums[i]
            if curr - k in prefix:
                ans += prefix[curr - k]
            prefix[curr] = prefix.get(curr, 0) + 1
        return ans 
        