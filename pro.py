def factorialN(n):
    if n < 0:       # factorial for -ve number is 0
        return 0
    if n == 0 or n == 1:   # factorial for 0 and 1 is one
        return 1
    else:
        fact = 1 
        for i in range(2,n + 1): # initialize from 2 to n
            fact *= i
        return fact

n = int(input("calculate the factorial of the number: "))

print(factorialN(n))
