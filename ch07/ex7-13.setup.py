# 예제 7-13 Cython을 위한 OpenMP 컴파일러와 링커 플래그를 setup.py에 추가하기

#setup.py
from distuitls.core import setup
from distuitls.extension import Extension
from Cython.Distutils import build_ext

setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = [Extension("calculate",
                             ["cython_np.pyx"],
                             extra_compile_args=['-fopenmp'],
                             extra_link_args=['-fopenmp'])]
)
