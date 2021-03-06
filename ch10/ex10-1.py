# 예제 10-1 Parallel Python 로컬 예제

...
import pp

NBR_ESTIMATES = 1e8

def calculate_pi(nbr_estimates):
    steps = range(int(nbr_estimates))
    nbr_trails_in_unit_circle = 0
    for step in steps:
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        is_in_unit_circle = x * x + y * y <= 1.0
        nbr_trails_in_unit_circle += is_in_unit_circle
    return nbr_trails_in_unit_circle

if __name__ == "__main__":
    NBR_PROCESSES = 4
    job_server = pp.Server(ncpus=NBR_PROCESSES)
    print("Starting pp with {} local workers".format(job_server.get_ncpus()))
    nbr_trails_per_process = [NBR_ESTIMATES] * NBR_PROCESSES
    jobs = []
    for input_args in nbr_trails_per_process:
        job = job_server.submit(calculate_pi, (input_args,), (), ("random",))
        jobs.append(job)
    # 결과가 준비될 때가지 각 작업은 블록된다.
    nbr_in_unit_circles = [job() for job in jobs]
    print("Amount of work:", sum(nbr_trails_per_process))
    print(sum(nbr_in_unit_circles) * 4 / NBR_ESTIMATES / NBR_PROCESSES)
