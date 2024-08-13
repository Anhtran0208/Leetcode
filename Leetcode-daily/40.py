"""
Problem: Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(curr_arr, remain, idx):
            if remain == 0:
                ans.append(curr_arr[:])
                return
            if remain < 0:
                return
            for i in range (idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                curr_arr.append(candidates[i])
                backtrack(curr_arr, remain - candidates[i], i+1)
                curr_arr.pop()
        candidates.sort()
        backtrack([], target, 0)
        return ans