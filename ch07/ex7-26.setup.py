# 예제 7-26 CPython 모듈의 확산 인터페이스를 위한 설정 파일

"""
CPython 확산 모듈을 위한 setup.py, 이 확장은 다음과 같이 빌드할 수 있다.

    $ python setup.py build_ext --inplace

이 명령은 파이썬에서 바로 임포트할 수 있는 cdiffusion.so 파일을 생성한다.
"""

from distutils.core import setup, Extension
import numpy.distutils.misc_util

__version__ = "0.1"

cdiffusion = Extension(
    'cdiffusion',
    sources = ['cdiffusion/cdffusion.c', 'cdiffusion/python_interface.c'],
    extra_compile_args = ["-03", "-std=c99", "-Wall", "-p", "-pg", ],
    extra_link_args = ["-lc"],
)
setup (
    name = 'diffusion',
    version = __version__
    ext_modules = [cdiffusion,],
    packages = ["diffusion", ],
    include_dirs = numpy.distutils.misc_util.get_numpy_include_dirs(),
)
