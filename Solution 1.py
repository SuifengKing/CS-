class Solution(object):
    def minimumTimeRequired(self, jobs, k):
        """
        :type jobs: List[int]
        :type k: int
        :rtype: int
        """
        n = len(jobs)
        workers = [0 for i in range(n)]
        def fun(index, workers, jobs, n, res):
            if index==n:    # 全部工作分配完成时，更新结果
                if max(workers)<res[0]:
                    res[0] = max(workers)
            else:
                for i in range(k):
                    # 优化，当工人i还没被分配工作时，我们不给工人i+1分配工作
                    if i>0 and workers[i-1]==0:
                        break
                    workers[i]+=jobs[index]
                    if workers[i]<res[0]:   # 如果分配结果大于当前最优，跳过本次分配
                        fun(index+1, workers, jobs, n, res)
                    workers[i]-=jobs[index]
        res = [float('inf')]
        
        fun(0, workers, jobs, n, res)
        return res[0]

    
