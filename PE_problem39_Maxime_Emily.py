#If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
#
#{20,48,52}, {24,45,51}, {30,40,50}
#
#For which value of p ≤ 1000, is the number of solutions maximised?



MaxPerimeter = 1000
MaxNumberOfTriplets= 0
perimeter =1
Solution =0
while perimeter<=MaxPerimeter:
    b=1
    NumberOfTriplets = 0
    perimeter_divided_by_2 = perimeter//2
    while b<perimeter_divided_by_2:
        a=1
        while a<=b and perimeter-a >2*b:
            c = perimeter -b -a
            if b**2+a**2== c**2:
                NumberOfTriplets+=1
            a+=1
        b+=1
    if NumberOfTriplets>MaxNumberOfTriplets:
        MaxNumberOfTriplets= NumberOfTriplets
        Solution = perimeter
    perimeter+=1
print(MaxNumberOfTriplets)
print(Solution)
        

