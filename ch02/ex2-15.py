# 예제 2-15 적절한 지점에서 dowser를 실행해서 웹 서버 활성화하기

...
        for xcoord in x:
            zs.append(complex(xcoord, ycoord))
            cs.append(complex(c_real, c_imag))

    launch_memory_usage_server()

...
    output = calculate_z_serial_purepython(max_iterations, zs, cs)
...
    print("now waiting...")
    while True:
        time.sleep(1)
