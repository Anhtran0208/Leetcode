"""
Problem:
You are given an integer array bloomDay, an integer m and an integer k.

You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.
"""
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def totalBouquets(days, bloomDay, k):
            cnt_flower = 0 
            cnt_bouquet = 0
            for i in range (len(bloomDay)):
                if days >= bloomDay[i]:
                    cnt_flower +=1
                else:
                    cnt_flower = 0 
                if cnt_flower == k:
                    cnt_bouquet +=1
                    cnt_flower = 0 
            return cnt_bouquet
        
        if k * m > len(bloomDay):
            return -1
        left = 0 
        right = max(bloomDay)
        ans = max(bloomDay)
        while left <= right:
            mid = (left + right) // 2
            if totalBouquets(mid, bloomDay, k) >= m:
                ans = min(ans, mid)
                right = mid - 1
            else:
                left = mid + 1
        return ans

        