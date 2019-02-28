#include <math.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include "sample.h"

/*
 char             -128 ~ +127        (1 Byte)
 short             -32767 ~ + 32768    (2 Bytes)
 unsigned short     0 ~ 65536        (2 Bytes)
 int             -2147483648 ~ +2147483647   (4 Bytes)
 unsigned int         0 ~ 4294967295    (4 Bytes)
 long == int
 long long         -9223372036854775808 ~ +9223372036854775807    (8 Bytes)
 double         1.7 * 10^308        (8 Bytes)
 * */


void testInt(long long num){
    printf("long -- %lld\n" , num);
    printf("long long %lld \n" , num);
}

long long fib(unsigned int n){
    if (n<=0) {
        return -1;
    }
    if (n<=2) {
        return 1; 
    }
    long long a1 = 1;
    long long a2 = a1;
    for (int i = 2; i <= n; ++i) { 
        long long tmp = a2;
        a2 = a1 + a2;
        a1 = tmp;
    }

    sleep(1);
    return a2;
}

char* some_wasting_time_op(int n){
    sleep(n);
    return "Done.\n";
}


int main(int argc, char *argv[])
{
    unsigned int n = 10;
    printf("fib %d is %lld\n", n,fib(n));
    printf(some_wasting_time_op(2));
    return 0;
}
