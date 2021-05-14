class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        jobLen = len(jobs)
        state_jobsum = [0 for _ in range(1 << jobLen)]
        for i in range(jobLen):
            for j in range(1 << i):
                state_jobsum[(1 << i) + j] = jobs[i] + state_jobsum[j]

        dp = [[0 for _ in range(1 << jobLen)] for _ in range(k)]
        for i in range(1 << jobLen):
            dp[0][i] = state_jobsum[i]

        for i in range(1, k):
            for j in range(1 << jobLen):
                minval = float('inf')
                x = j
                while x != 0:
                    cur = max(state_jobsum[x], dp[i-1][j-x])
                    minval = min(minval, cur)
                    x = (x - 1) & j
                dp[i][j] = minval
        
        return dp[k-1][(1 << jobLen) - 1]
