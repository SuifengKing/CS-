class Solution 
{
public:
    int minimumTimeRequired(vector<int>& jobs, int k) 
    {
        int n = jobs.size();
        vector<int> state_jobsum((1<<n), 0);
        for (int i = 0; i < n; i ++)
            for (int j = 0; j < (1 << i); j ++)
                state_jobsum[(1<<i) + j] = jobs[i] + state_jobsum[j];
            
        vector<vector<int>> dp(k, vector<int>((1<<n), 0));
        for (int state = 0; state < (1<<n); state ++)
            dp[0][state] = state_jobsum[state];
        
        for (int i = 1; i < k; i ++)
        {
            for (int state = 0; state < (1<<n); state ++)
            {
                int minval = INT_MAX;
                int x = state;
                while(x != 0)
                {
                    int cur = max(dp[i-1][state-x], state_jobsum[x]);
                    minval = min(minval, cur);
                    x = (x - 1) & state;
                }
                dp[i][state] = minval;
            }
        }

        return dp[k-1][(1<<n) - 1];
    }
};
