import bisect

def jobScheduling(startTime, endTime, profit):
    # Step 1: Combine the jobs and sort by end time
    jobss = sorted(zip(startTime, endTime, profit),key=lambda x:x[1])
    jobs = list(zip(startTime, endTime, profit))
    print(jobss)
    print(jobs)
    # Step 2: Initialize dp with dummy value [endTime, profit]
    dp = [[0, 0]]  # [end, max_profit]

    # Step 3: Process each job
    for s, e, p in jobs:
        print(s,e,p) 
        # Find latest job that ends before current job starts
        i = bisect.bisect(dp, [s + 1]) - 1
        print("i:",dp,[s+1])

        # If taking this job gives better profit, add to dp
        if dp[i][1] + p > dp[-1][1]:
            dp.append([e, dp[i][1] + p])
        print("Dp:",dp)
    return dp[-1][1]

startTime = [1, 2, 3, 3]
endTime   = [3, 4, 5, 6]
profit    = [50, 10, 40, 70]

print(jobScheduling(startTime,endTime,profit))
