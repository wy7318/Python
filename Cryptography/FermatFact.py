import math

def fermat(n):
    for p in range(1,101):
        q = n + p**2
        if math.sqrt(q) % 1 == 0:
            return p, int(math.sqrt(q))


print(fermat(91))
