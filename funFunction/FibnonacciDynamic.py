def fib(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    bottom = [None]*(n+1)
    bottom[1] = 1
    bottom[2] = 1
    for i in range(3, n+1):
        bottom[i] = bottom[i-1]+bottom[i-2]
    return bottom[n]
print(fib(3000))
