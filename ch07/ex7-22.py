# 예제 7-22 cffi 2D 확산 코드

from cffi import FFI

ffi = FFI()
ffi.cdef(r'''
    void evolve(
      int Nx, int Ny,
      double **in, double **out,
      double D, double dt
    );
''')
lib = ffi.dlopen("../diffusion.so")

def evolve(grid, dt, out, D=1.0):
    X, Y = grid_shape
    pointer_grid = ffi.cast('double**', grid.ctypes.data)
    pointer_out = ffi.cast( 'double**',  out.ctypes.data)
    lib.evolve(X, Y, pointer_grid, pointer_out, D, dt)
