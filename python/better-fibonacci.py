def better_fibonacci(n):
    if n < 2:
        return n

    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b

    return b

for i in range(10):
    print(better_fibonacci(i))
# 0 1 1 2 3 5 8 13 21 34
