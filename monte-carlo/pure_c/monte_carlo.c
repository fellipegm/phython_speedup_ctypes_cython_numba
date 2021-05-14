#include <stdio.h>
#include <stdlib.h>

double dice6(int N, int ndice, int nsix)
{
    int M = 0;
    int six, r, i, j;
    double p;
    for (i = 0; i < N; i++) {
        six = 0;
        for (j = 0; j < ndice; j++) {
            r = 1 + (int) (6*(rand()/((double)RAND_MAX))); /* roll die no. j */
            if (r == 6)
                six += 1;
            }
            if (six >= nsix)
                M += 1;
    }
    p = ((double) M)/N;
    return p;
}

int main(int nargs, const char* argv[])
{
    int N = atoi(argv[1]);
    int ndice = 2;
    int nsix = 2;
    double p = dice6(N, ndice, nsix);
    printf("C code: N=%d, p=%f\n", N, p);
    return 0;
}