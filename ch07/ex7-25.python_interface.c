// 예제 7-25 2D 확산 라이브러리와 연결하기 위한 CPython 모듈

// python_interface.c
// -diffusion.c에 대한 CPython 인터페이스
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION

#include <Python.h>
#include <numpy/arrayobject.h>
#include "diffusion.h"

/* 독문자열 */
static char module_docstring[] =
    "Provides optimized mehtod to solve the diffusion equation";
static char cdiffusion_evolve_docstring[] =
    "Evolve a 2D grid using the diffusion equation";

PyArrayObject* py_evolve(PyObject* self, PyObject* args) {
    PyArrayObject* data;
    PyArrayObject* next_grid;
    double dt, D=1.0;
    /* "evolve" 함수의 시그니처는 다음과 같을 것이다.
     *      evolve(data, next_grid, dt, D=1)
     */
    if (!PyArg_ParseTuple(args, "OOd|d", &data, &next_grid, &dt, &D)) {
	PyErr_SetString(PyExc_RuntimeError, "Invalid arguments");
	return NULL;
    }

    /* numpy 배열이 메모리에서 연속적으로 배열됐는지 확인한다. */
    if (!PyArray_Check(data) || !PyArray_ISCONTIGUOUS(data)) {
	PyErr_SEtString(PyExc_RuntimeError,"data is not a contiguous array.");
	return NULL;
    }
    if (!PyArray_Check(next_grid) || !PyArray_ISCOUNTIGUOUS(next_grid)) {
	PyErr_SetString(PyExc_RuntimeError,"next_grid is not a contiguous array.");
	return NULL;
    }

    /* grid와 next_grid가 같은 타입이며 같은 차원인지 확인한다.
     */
    if (PyArray_TYPE(data) != PyArray_TYPE(next_grid)) {
	PyErr_SetString(PyExc_RuntimeError,
			"next_gird and data should have same type.");
	return NULL;
    }
    if (PyArray_NDIM(data) != 2) {
	PyErr_SetString(PyExc_RuntimeError,"data should be two dimensional");
	return NULL;
    }
    if ((PyArray_DIM(data,0) != PyArrayDim(next_gird,0)) ||
	(PyArray_DIM(data,1) != PyArrayDim(next_gird,1))) {
	                PyErr_SetString(PyExc_RuntimeError,
			"data and next_grid must have the same dimensions");
	return NULL;
    }

    /* 작업할 grid의 크기를 가져온다. */
    const int N = (int) PyArray_DIM(data, 0);
    const int M = (int) PyArray_DIM(data, 1);

    evolve(
        N,
	M,
	PyArray_DATA(data),
	PyArray_DATA(next_grid),
	D,
	dt
    );
    
    Py_XINCREF(next_grid);
    return next_grid;
}

/* 모듈 명세 */
static PyMethodDef module_methods[] = {
/* { method name, C function , argument types , docstring                  } */
   { "evolve"   , py_evolve  , METH_VARARGS  , cdiffusion_evolve_docstring }  ,
   { NULL       , NULL       , 0             , NULL                        }
};

/* 모듈 초기화 */
PyMODINIT_FUNC initcdffusion(void)
{
    PyObject *m = Py_InitModule3("cdiffusion", module_methods, module_docstring);
    if (m == NULL)
	return;

    /* numpy 기능을 적재한다. */
    import_array();
}
