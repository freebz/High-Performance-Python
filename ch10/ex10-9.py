# 예제 10-9 로컬 클러스터를 사용해 원주율 추정하기

from ipyparallel import Client, require
NBR_ESTIMATES = 1e8

@require('random')
def calculate_pi(nbr_estimates):
    ...
    return nbr_trails_in_unit_circle

if __name__ == "__main__":
    c = Client()
    nbr_engines = len(c.ids)
    print("We're using {} engines".format(nbr_engines))
    dview = c[:]
    nbr_in_unit_circles = dview.apply_sync(calculate_pi, NBR_ESTIMATES)

    print("Estimates made:", nbr_in_unit_circles)

    # 엔진망을 사용해 작업을 수행한다.
    nbr_jobs = len(nbr_in_unit_circles)
    print(sum(nbr_in_unit_circles) * 4 / NBR_ESTIMATES / nbr_jobs)
