﻿#Written by Yunfei LIU
#Sep 13, 2020

#Please read the disclaimer
'''Another example
#input a four-digit long integer
Number = int(input())
#sperate digits by floor division
Digit1 = Number//1000
Digit2 = Number//100 - Digit1*10
Digit3 = Number//10 - Digit1*100 - Digit2*10
Digit4 = Number - Digit1*1000 - Digit2*100 - Digit3*10
#add up the digits
Sum = Digit1 + Digit2 + Digit3 + Digit4
#output the answer
print(Sum)
'''

#input an int
number = int(input())
#seperate all the digits
digit1 = number%10
digit2 = (number%100 - digit1)/10
digit3 = (number%1000 - digit2*10 - digit1)/100
digit4 = (number - digit3*100 -digit2*10 - digit1)/1000
#transform them into integer
intdigit1 = int(digit1)
intdigit2 = int(digit2)
intdigit3 = int(digit3)
intdigit4 = int(digit4)
#add up all the digits
add = int(intdigit1 + intdigit2 + intdigit3 + intdigit4)
#output the answer
print(add)
