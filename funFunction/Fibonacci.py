def fibonacci(a):
    if a==0:
        return 0
    elif a ==1:
        return 1
    elif a>=2:
        return fibonacci(a-1)+fibonacci(a-2)

num = int(input())
print(fibonacci(num))
