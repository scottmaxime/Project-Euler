# Take the number 192 and multiply it by each of 1, 2, and 3:
#
# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
#
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
#
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

#Initialize variables
Solution = 123456789
#We start at 2 since 1 will give us 123456789
FixNumber = 2
LengthOfConcatenatedProduct = 0

#We notice that since n >=2, the concatenation of FixNumber & FixNumber*2 has at least twice the length of FixNumber. Therefore, FixNumber has at most 4 digits.
while FixNumber <= 9999:
    #We initialize the concatenated Product and the index
    concatenatedProduct = str(FixNumber)
    index = 2
    #We create a loop which concatenates the next multiple of FixNumber until the length of concatenatedProduct is at least 9.
    while len(concatenatedProduct) < 9:
        concatenatedProduct = str(concatenatedProduct) + str(FixNumber*index)
        index+=1
    #We check if the length is 9 and if it is a pandigital number bigger than our solution
    if len(concatenatedProduct) == 9 and set(concatenatedProduct)==set("123456789")  and int(concatenatedProduct) > Solution:
        Solution = int(concatenatedProduct)
    FixNumber += 1

print(Solution)
        

    


        

