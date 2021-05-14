import random
import math


class Solution(object):
    def minimumTimeRequired(self, jobs, k):
        """
        :type jobs: List[int]
        :type k: int
        :rtype: int
        """
        n = len(jobs)
        global ans
        global _jobs
        ans = float('inf')
        _jobs = jobs

        # 最高温 / 最低温
        high = 1E4
        low = 1E-4
        # 变化速率（以什么速度进行退火，系数越低退火越快，迭代次数越少，落入「局部最优」（WA）的概率越高；系数越高TLE风险越大）
        fa = 0.6
        # 迭代次数
        N = 400

        def calc():
            global _jobs
            # 计算当前jobs序列对应的最小「最大工作时间 」是多少
            works = [0]*15
            for i in range(n):
                # [固定模式分配逻辑]: 每次都找最小的worker去分配
                idx = 0
                cur = works[idx]
                for j in range(k):
                    if works[j] < cur:
                        cur = works[j]
                        idx = j
                works[idx] += _jobs[i]
            cur = 0
            for i in range(k):
                cur = max(cur, works[i])
            global ans
            ans = min(ans, cur)
            return cur

        def sa():
            global _jobs
            t = high
            while t > low:
                a = random.randint(0, n-1)
                b = random.randint(0, n-1)
                prev = calc()
                _jobs[a], _jobs[b] = _jobs[b], _jobs[a]
                cur = calc()
                diff = prev - cur
                # 退火为负收益（温度上升），以一定概率回退现场
                # print(diff)
                if diff > 0 and math.log(diff/t, math.e) < random.random():
                    _jobs[a], _jobs[b] = _jobs[b], _jobs[a]
                t *= fa

        while N > 0:
            sa()
            N -= 1
        return ans
