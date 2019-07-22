# program to print fibonacci series 0 1 1 2 3 5 8 13 21 34 55 89 141.......

def fibo(n):
    if n <= 0:
        print("Incorrect output!! Enter number greater than zero")
    elif n == 1:
        return 0
    elif n==2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

n = int(input("Enter the number of terms: "))

print(fibo(n))




