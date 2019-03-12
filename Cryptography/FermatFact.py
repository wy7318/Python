import math

def fermat(n):
    for p in range(1,10000):
        q = n + p**2
        if math.sqrt(q) % 1 == 0:
            return int(math.sqrt(q)) + p, int(math.sqrt(q)) - p


print(fermat(8777))
