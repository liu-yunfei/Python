﻿# Written by Yunfei LIU
# Oct 8, 2020
# Please obey the license GPLv3

#Get the input for the puzzle
n = int(input('Enter n: '))
x = y = 1
#Start a loop to enumerate all the possible situations
#enum y
for i in range(n):
    x = 1
    #enum x
    for j in range(n):
        #Output if the answer matches
        if (x**0.5)+(y**0.5)==(n**0.5):
            print('A possible solution is',x,'and',y,'for n=',n)
        x += 1
        #To make sure x is the smaller one
        if x>y:
            break
    y += 1


#Another more effective way

#Create a function to meet the requirement
def iszero(test):
    if test>(-10**-10) and test<(10**-10):
        return True
    else:
        return False

#Get the input
n = int(input('Enter an integer: '))
#Exclude the special situation
import sys
if n < 2:
    sys.exit(0)
x = 1
nvalue = n**0.5
#Define the border of the larger component
left = x
right = n
#Find the number in the middle of the border
mid = (left+right+1)//2
#Start to enumerate x
for i in range((n+1)//2):
    xvalue = x**0.5
    #Start to narrow the border
    while (right-left)!=1:
        if xvalue + mid**0.5 - nvalue > 0:
            right = (right+left+1)//2
        #Output when matched
        elif iszero(xvalue + mid**0.5 - nvalue):
            print('A possible solution is',x,'and',mid)
            break
        else:
            left = (right+left)//2
        mid = (left+right+1)//2
    #reset the border for the next time narrowing
    right = n
    left = x
    x += 1
