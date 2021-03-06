﻿# Written by Yunfei LIU
# Oct 8, 2020
# Please obey the license GPLv3

#Create a function to meet the requirement of the question
def chr8(n):
    Dec = 0
    for i in range(len(n)):
        Dec = Dec + int(n[len(n)-1-i])*(2**i)
    Cha = chr(Dec)
    return Cha

#Input an integer
N = int(input('Input an integer: '))
#Convert it into binery and save it into a list
BinStrRev = []
Digit = 0
while N != 0:
    Digit = N%2
    N = N//2
    BinStrRev.append(Digit)
#Change the reversed list into positive sequence
BinStr = []
length = len(BinStrRev)
for i in range(length):
    BinStr.append(BinStrRev[length-i-1])
#Split the list into 8 digits and transform it into char
k = 0
CharList = []
for j in range((length//8)+1):
    BinList = BinStr[k:k+7]
    CharList.append(chr8(BinList))
    k += 8
print(''.join(CharList))
