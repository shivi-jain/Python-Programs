#Program to check if the given number is a fibonacci number

import math

def CheckPerfectSquare(x):
    i = int(math.sqrt(x))
    return (x == i*i)

def CheckFibo(n):
    if(CheckPerfectSquare(5*n*n + 4) or CheckPerfectSquare(5*n*n - 4)):
        print("Fibonacci : Yes")
    else:
        print ("Fibonacci : No")

n = int(input("Enter the number: "))

print(CheckFibo(n))

