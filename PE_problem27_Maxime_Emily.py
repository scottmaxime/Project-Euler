'''
Euler discovered the remarkable quadratic formula:

        n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive integer values 0 <= n <= 39. However, when n=40, 40^2 + 40 + 41 
is divisible by 41, and certainly when n = 41, 41^2 + 41 +41 is clearly divisible by 41.

The incredible formula n^2 - 79 n + 1601 was discovered, which produces 80 primes for the consecutive values 0 <= n <= 79. The product 
of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

        n^2 + an + b, where |a| < 1000 and |b| <= 1000, 
        
where |n| is the modulus/absolute value of n 
e.g. |11| = 11 and |-4| = 4 
Find the product of the coefficients, a and b, for the quadratic expression that produces the 
maximum number of primes for consecutive values of n, starting with n = 0.
'''
import math


def checkIfPrime(ourNumber):
    index = 2
    if ourNumber <= 1:
        return False
    while index <= ourNumber:
        HighestPossibleDivisor = int(math.sqrt(ourNumber))

        if index > HighestPossibleDivisor:
            index = ourNumber
            return True
        elif ourNumber%index == 0 :
            #To break out of the while loop
            index = ourNumber
            return False
        if index == 2:
            index += 1
        else:
            #If not divisible by two, it can't be divisible by any other even number
            index += 2

n = 0
highestConsecutiveValue = 0
ProductOfCoefficients = 0
isPrime = True

for a in range(-999,1000):
    for b in range(-1000,1001):
        isPrime = True
        n = 0
        while isPrime:
            isPrime = checkIfPrime(n**2 + a*n +b)
            n += 1
        if  n-1 > highestConsecutiveValue:
            highestConsecutiveValue = n-1
            ProductOfCoefficients = a*b



print(ProductOfCoefficients)


    
        
            
            
