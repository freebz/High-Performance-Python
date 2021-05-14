# 예제 7-4 Cython을 이용하여 cythonfn.pyx를 C 코드로 변경하는 setup.py 스크립트

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = [Extension("calculate",["cythonfn.pyx"])]
    )
