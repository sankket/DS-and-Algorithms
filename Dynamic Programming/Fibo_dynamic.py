import time

def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

cache = {}

def fibo_dynamic(n):
    if n in cache:
        return cache[n]
    else:
        if n < 2:
            return n
        else:
            cache[n] = fibo_dynamic(n-1) + fibo_dynamic(n-2)
            return cache[n]

t1 = time.time()
print(fibonacci(30))
t2 = time.time()
print(t2-t1)

t1 = time.time()
print(fibo_dynamic(30))
t2 = time.time()
print(t2-t1)

