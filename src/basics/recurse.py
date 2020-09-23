def fact(n):
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


def fib(n):
    if n >= 3:
        return fib(n - 1) + fib(n - 2)
    else:
        return 1


def fibbi(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
        
# for i in range(130):
    # print(i, factorial(i))

for i in range(1, 30):
    print(i, fibbi(i))
