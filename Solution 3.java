class Solution {
    int[] jobs;
    int[] works = new int[20];
    int n, k;
    int ans = 0x3f3f3f3f;    
    Random random = new Random(20210508);
    // 最高温/最低温/变化速率（以什么速度进行退火，系数越低退火越快，迭代次数越少，落入「局部最优」（WA）的概率越高；系数越高 TLE 风险越大）
    double hi = 1e4, lo = 1e-4, fa = 0.90; 
    // 迭代次数，与变化速率同理
    int N = 400; 

    // 计算当前 jobs 序列对应的最小「最大工作时间 」是多少
    int calc() {
        Arrays.fill(works, 0);
        for (int i = 0; i < n; i++) {
            // [固定模式分配逻辑] : 每次都找最小的 worker 去分配
            int idx = 0, cur = works[idx];
            for (int j = 0; j < k; j++) {
                if (works[j] < cur) {
                    cur = works[j];
                    idx = j;
                }
            }
            works[idx] += jobs[i];
        }
        int cur = 0;
        for (int i = 0; i < k; i++) cur = Math.max(cur, works[i]);
        ans = Math.min(ans, cur);
        return cur;
    }
    void swap(int[] arr, int i, int j) {
        int c = arr[i];
        arr[i] = arr[j];
        arr[j] = c;
    }
    void sa() {
        for (double t = hi; t > lo; t *= fa) {
            int a = random.nextInt(n), b = random.nextInt(n);
            int prev = calc(); // 退火前
            swap(jobs, a, b);
            int cur = calc(); // 退火后
            int diff = prev - cur;
            // 退火为负收益（温度上升），以一定概率回退现场
            if (Math.log(diff / t) < random.nextDouble()) { 
                swap(jobs, a, b);
            }
        }
    }
    public int minimumTimeRequired(int[] _jobs, int _k) {
        jobs = _jobs;
        n = jobs.length;
        k = _k;
        while (N-- > 0) sa();
        return ans;
    }
}
