#Solution to Euler Problem 3
#
#
#
#The prime factors of 13195 are 5, 7, 13 and 29.
#
#What is the largest prime factor of the number 600851475143 ?

import math
PrimeDivisors = []
index = 2
ourNumber = 600851475143



while index <= ourNumber:
    HighestPossibleDivisor = int(math.sqrt(index))
    if ourNumber%index == 0:
        PrimeDivisors.append(index)
        while ourNumber%index == 0:
            ourNumber = ourNumber/index
    index += 1

#print(PrimeDivisors)
print(max(PrimeDivisors))
