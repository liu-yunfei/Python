﻿#Input an integer and print all primes smaller than it
print('Written by Yunfei LIU\nOct 12, 2020')
Max = int(input('Please input an integer: '))
#Use sieve of Eratosthenes to find primes
MaxRange = int(Max**0.5+1)
PrimeList = []
for i in range(Max):
    PrimeList.append(True)
#If the subscript is not a prime, change the value to False
PrimeList[0] = False
for i in range(MaxRange):
    if PrimeList[i] == False:
        continue
    else:
        for j in range(Max//(i+1)-1):
            PrimeList[(i+1)*(j+2)-1] = False
#Output the Trues' subscript
ResultList = []
for i in range(Max):
    if PrimeList[i] == True:
        ResultList.append(i+1)
print(ResultList)
