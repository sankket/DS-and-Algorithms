# The Recursive Method.
# Fibonacci Series - 0 1 1 2 3 5 8 13 21 34 55 . . . .
def fibonacci(index):
    if index == 0:
        return 0
    elif index == 1:
        return 1
    else:
        return fibonacci(index-1) + fibonacci(index-2)

print(fibonacci(7))

# Iterative method.
def iter_fibo(index):
    num1 = 0
    num2 = 1
    if index == 0:
        return num1
    if index == 1:
        return num2
    for i in range(2,index+1):
        temp = num1+num2
        num1 = num2
        num2 = temp
    return temp

print(iter_fibo(8))


# The complexity of Recursive algorithms is 2^n exponentially increases.
