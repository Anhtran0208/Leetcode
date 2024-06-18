"""
Problem:
You have n jobs and m workers. You are given three arrays: difficulty, profit, and worker where:

difficulty[i] and profit[i] are the difficulty and the profit of the ith job, and
worker[j] is the ability of jth worker (i.e., the jth worker can only complete a job with difficulty at most worker[j]).
Every worker can be assigned at most one job, but one job can be completed multiple times.

For example, if three workers attempt the same job that pays $1, then the total profit will be $3. If a worker cannot complete any job, their profit is $0.
Return the maximum profit we can achieve after assigning the workers to the jobs.
"""
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        job_profit = []
        for i in range (len(profit)):
            job_profit.append((difficulty[i], profit[i]))
        job_profit.sort()
        for i in range (len(job_profit) - 1):
            job_profit[i+1] = (job_profit[i+1][0], max(job_profit[i][1], job_profit[i+1][1]))
        ans = 0
        for i in range (len(worker)):
            left, right = 0, len(job_profit) - 1
            curr_profit = 0
            while left <= right:
                mid = (left + right) // 2
                if job_profit[mid][0] <= worker[i]:
                    curr_profit = max(curr_profit, job_profit[mid][1])
                    left = mid + 1
                else:
                    right = mid - 1
            ans +=curr_profit
        return ans 
        