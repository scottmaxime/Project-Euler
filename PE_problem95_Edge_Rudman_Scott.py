'''
The proper divisors of a number are all the divisors excluding the number itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As the sum of these divisors is 
equal to 28, we call it a perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220, forming a chain of two numbers. For this reason, 220 and 284 
are called an amicable pair.

Perhaps less well known are longer chains. For example, starting with 12496, we form a chain of five numbers:

12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)

Since this chain returns to its starting point, it is called an amicable chain.

Find the smallest member of the longest amicable chain with no element exceeding one million.
'''

import numpy

def properPrimeDivisors(number):
    listOfProperPrimeDivisors = []
    squareRootOfNumber = number**(1/2)
    currentNumber = number
    for index in range(2 , int(squareRootOfNumber)+2):
        isCurrentNumberPrime = True
        while currentNumber%index == 0 :
            listOfProperPrimeDivisors.append(index)
            currentNumber = int(currentNumber/index)
            isCurrentNumberPrime = False
    if isCurrentNumberPrime and currentNumber != number and currentNumber != 1:
        listOfProperPrimeDivisors.append(currentNumber)
    return listOfProperPrimeDivisors

def numberToBinary(number):
    binaryNumber = list(str(bin(number)))
    return binaryNumber[2:]


def powerset(listOfNumber):
    setOfPossibleDivisors = set()
    numberOfPrimeDivisors = len(listOfNumber)
    for index in range(1,2**numberOfPrimeDivisors-1):
        index2 = 1
        addedList = []
        binaryKey = numberToBinary(index)
        lengthOfBinaryKey = len(binaryKey)
        while index2 <= lengthOfBinaryKey:
            if binaryKey[-index2] == '1':
                addedList.append(listOfNumber[index2-1])
            index2 +=1
        numberToAdd = numpy.prod(addedList)
        setOfPossibleDivisors.add(numberToAdd)
    setOfPossibleDivisors.add(1)
    return setOfPossibleDivisors

def setOfDivisors(number):
    listOfDivisors=[1]
    for i in range(2,int(number**(1/2))+1):
        if number%i == 0:
            listOfDivisors.append(i)
            listOfDivisors.append(int(number/i))
    return listOfDivisors


def chainOfNumbers(number):
    currentNumber = number
    returnList = []
    dictionaryOfNumbers = {}
    while dictionaryOfNumbers.get(currentNumber,0) == 0 and currentNumber < 1000000 and currentNumber >= number:
        returnList.append(currentNumber)
        dictionaryOfNumbers[currentNumber] = 1
        currentNumber = sum(setOfDivisors(currentNumber))
    return returnList

def isChainAmicable(chain):
    booleanOutput = False
    if sum(setOfDivisors(chain[-1])) == chain[0]:
        booleanOutput = True
    return booleanOutput




maximumLength = 0
for index in range(1,1000000):
    currentLength = len(chainOfNumbers(index))
    currentList = chainOfNumbers(index)
    minimalMemberMaxChain = 0
    if isChainAmicable(currentList) and currentLength > maximumLength:
        print('Index = '+ str(index))
        maximumLength = currentLength
        minimalMemberMaxChain = index
        maximalChain = currentList



    


print(maximalChain)




