"""
Problem:
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.
"""
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        odds = 0
        ans = 0 
        cnt = 0
        for i in range (len(nums)):
            if nums[i] % 2 == 1:
                odds +=1
            if odds == k:
                cnt = 0 
                while odds == k:
                    if nums[left] % 2 == 0:
                        cnt +=1
                    else:
                        cnt +=1
                        odds -=1
                    left +=1
            ans += cnt
        return ans
