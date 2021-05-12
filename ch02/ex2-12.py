# 예제 2-12 heapy를 사용해서 코드가 실행되는 동안 객체 개수가 변하는 과정 살펴보기

def calc_pure_python(draw_output, desired_width, max_iterations):
    ...
    while xcoord < x2:
        x.append(xcoord)
        xcoord += x_step

    from guppy import hpy; hp = hpy()
    print("heapy after creating y and x lists of floats")
    h = hp.heap()
    print(h)
    print()

    zs = []
    cs = []
    for ycoord in y:
        for xcoord in x:
            zs.append(complex(xcoord, ycoord))
            cs.append(complex(c_real, c_imag))

    print("heapy after creating zs and cs using complex numbers")
    h = hp.heap()
    print(h)
    print()

    print("Length of x:", len(x))
    print("Total elements:", len(zs))
    start_time = time.time()
    output = calculate_z_serial_purepython(max_iterations, zs, cs)
    end_time = time.time()
    secs = end_time - start_time
    print(calculate_z_serial_purepython.__name__ + "took", secs, "seconds")

    print()
    print("heapy after calling calculate_z_serial_purepython")
    h = hp.heap()
    print(h)
    print()
