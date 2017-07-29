#include <assert.h>

// tail recursive. optimized by C.
int fib(int n){
    if (n < 2) return n;

    return fib(n - 1) + fib(n - 2);
}

int main() {
    assert(fib(0) == 0);
    assert(fib(1) == 1);
    assert(fib(2) == 1);
    assert(fib(3) == 2);
    assert(fib(4) == 3);
    assert(fib(5) == 5);
    assert(fib(6) == 8);

    return 0;
}
