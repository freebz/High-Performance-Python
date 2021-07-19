# 예제 10-2 클러스터에서 Parallel Python 사용하기

...
NBR_JOBS = 1024
NBR_LOCAL_CPUS = 4
ppservers = ("*",) # 자동으로 발견할 IP 목록을 설정한다.
job_server = pp.Server(ppservers=ppservers, ncpus=NBR_LOCAL_CPUS)

print("Starting pp with {} local workers".format(job_server.get_ncpus()))
nbr_trails_per_process = [NBR_ESTIMATES] * NBR_JOBS
jobs = []
for input_args in nbr_trails_per_process:
    job = job_server.submit(calculate_pi, (input_args,), (), ("random",))
    jobs.append(job)
...
