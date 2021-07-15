# 예제 9-3 numpy를 사용해 원주율 추정하기

def estimate_nbr_points_in_quarter_circle(nbr_samples):
    # 각각이 새로운 프로세스에서 numpy를 위한 난수 시드를 설정한다.
    # 그렇지 않다면 포크(fork)로 만들어진 모든 프로세스가 동일한 상태를 공유한다.
    np.random.seed()
    xs = np.random.uniform(0, 1, nbr_samples)
    ys = np.random.uniform(0, 1, nbr_samples)
    estimate_inside_quarter_unit_circle = (xs * xs + ys * ys) <= 1
    nbr_trails_in_quater_unit_circle = np.sum(estimate_inside_quarter_unit_circle)
    return nbr_trails_in_quater_unit_circle
