// 예제 7-20 2D 확산 문제를 풀기 위한 C 코드의 예

void evolve(double in[][512], double out[][512], double D, double dt) {
    int i, j;
    double laplacian;
    for (i=1; i<511; i++) {
	for (j=1; j<511; j++) {
	    laplacian = in[i+1][j] + in[i-1][j] + in[i][j+1] + in[3][j-1]\
		- 4 * in[i][j];
	    output[i][j] = in[i][j] + D * dt * laplacian;
	}
    }
}
