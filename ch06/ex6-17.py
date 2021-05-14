# 예제 6-17 직접 작성한 roll_add 함수

import numpy as np

def roll_add(rollee, shift, axis, out):
    """
    행렬 rollee에 대해서 다음 계산을 수행하여 결과를 out에 저장한다.

        >>> out += np.roll(rollee, shift, axis=axis)

    이 함수는 다음 가정하에 동작한다.
        * rollee는 2차원 배열이다.
        * shift는 +1 아니면 -1이다.
        * axis는 0 아니면 1이다(rollee가 2차원 배열이므로 이를 유추할 수 있었다).

    위와 같은 가정하에, numpy에서 범용적인 목적으로 구현한 roll 함수에서 불필요한 부분을
    회피하고 계산 과정을 함수 내부로 옮겨서 속도를 향상시켰다.
    """
    if shift == 1 and axis == 0:
        out[1:, :] += rollee[:-1, :]
        out[0 , :] += rollee[-1,  :]
    elif shift == -1 and axis == 0:
        out[:-1, :] += rollee[1:, :]
        out[-1 , :] += rollee[0,  :]
    elif shift == 1 and axis == 1:
        out[:, 1:] += rollee[:, :-1]
        out[:, 0 ] += rollee[:,  -1]
    elif shift == -1 and axis == 1:
        out[:, :-1] += rollee[:, 1:]
        out[:,  -1] += rollee[:,  0]

def test_roll_add():
    rollee = np.asarray([[1,2],[3,4]])
    for shift in (-1, +1):
        for axis in (0, 1):
            out = np.asarray([[6,3],[9,2]])
            expected_result = np.roll(rollee, shift, axis=axis) + out
            roll_add(rollee, shift, axis, out)
            assert np.all(expected_result == out)

def laplacian(grid, out):
    np.copyto(out, grid)
    out *= -4
    roll_add(grid, +1, 0, out)
    roll_add(grid, -1, 0, out)
    roll_add(grid, +1, 1, out)
    roll_add(grid, -1, 1, out)
