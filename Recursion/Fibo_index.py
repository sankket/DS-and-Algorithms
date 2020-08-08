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
