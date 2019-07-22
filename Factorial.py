# Program to print the factorial of the given number:

import math

def Factorial(n):
    return 1 if(n==0 or n==1) else n*Factorial(n-1)

n = int(input("Enter the number: "))

print("Factorial is:",Factorial(n))

