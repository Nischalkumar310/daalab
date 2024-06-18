class Job:
    def __init__(self ,profit, deadline, q_no):
        self.profit = profit
        self.deadline = deadline
        self.q = q_no
def job_scheduling(jobs):
    jobs.sort(key = lambda job : job.profit, reverse = True)
    max_deadline = max(job.deadline for job in jobs)
    slots = [None]*max_deadline
    total_profit = 0
    scheduled_jobs = []
    for job in jobs:
        for j in range(job.deadline-1,-1,-1):
            if slots[j] is None:
                slots[j] = job
                total_profit += job.profit
                scheduled_jobs.append(job.q)
                break
    return total_profit, scheduled_jobs

n = int(input("Enter the number of Jobs: "))
jobs = []
print("Enter Pi: profit and Di: deadline for each Ji")
for i in range(n):
    profit, deadline = map(int, input().split())
    jobs.append(Job(profit, deadline, i + 1))

max_profit, scheduled_jobs_list = job_scheduling(jobs)

print("The Jobs subset is:", scheduled_jobs_list)
print("The max profit within deadline is:", max_profit)