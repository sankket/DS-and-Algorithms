# Fibonacci Series - 1,2,3,5,8,13,....
def fibonacci():
    n = int(input("Enter the terms :"))
    num1 = 0
    num2 = 1
    count = 0
    if n <= 0:
        print("Enter the valid number")
    if n == 1:
        print("Fibonacci sequence upto :")
        print(num1)
    else:
        print("Fibonacci Sequence")
        while count < n:
            print(num1)
            temp = num1 + num2
            num1 = num2
            num2 = temp
            count += 1


print(fibonacci())





