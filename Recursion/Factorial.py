# Finding the factorial of the number.
# both the recursive and ierative methods are added.
# The Iterative Method


def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact = fact * i
    return fact


print("The Answer by Iteration : ", factorial(5))

# The recursive Method.


def rec_fact(num):
    if num < 1:
        return 1
    else:
        return num * rec_fact(num - 1)

    
print("The Answer by recursion : ", rec_fact(5))
