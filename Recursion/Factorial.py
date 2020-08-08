# Finding the factorial of the number.
# The Iterative Method


def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact = fact * i
    return fact


print("The Answer by Iteration : ", factorial(5))
