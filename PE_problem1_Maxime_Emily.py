#Problem 1
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.
i = 1
MultiplesOf3or5 = []
while i<1000:
    if i%3 == 0 or i%5 == 0:
        MultiplesOf3or5.append(i)
        i+=1
    else:
        i+=1
print(sum(MultiplesOf3or5))