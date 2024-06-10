"""
Problem: 
Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

A subarray is a contiguous part of an array.
"""
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # (sum - prefix) %k = 0
        prefix = {0: 1}
        curr = 0 
        ans = 0 
        for i in range (len(nums)):
            curr += nums[i]
            remain = curr % k
            # remainder < 0
            if remain < 0:
                remain += k
            if remain in prefix:
                ans += prefix[remain] 
            prefix[remain] = prefix.get(remain, 0 ) + 1
        return ans 