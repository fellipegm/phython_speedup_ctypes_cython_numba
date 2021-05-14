

#include <stdio.h>
#include <stdlib.h>

int fofilter_pure_c(double *input, double *output, double dt, double tau, size_t n) {

    double a = tau / (tau + dt);
    double b = dt / (tau + dt);

    output[0] = 0;
    for (size_t i = 1; i < n; i++) {
        output[i] = input[i]*b + output[i-1]*a;
    }

    return 0;
}