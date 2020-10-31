# Written by Yunfei LIU
# Oct 8, 2020
# Please obey the license GPLv3

#Input a char
char = input("Input a letter: ")
num = ord(char)
#If it is a uppercase letter, start a uppercase loop
if 64<num and num<91:
    count = 0
    while num<91:
        print(count*' '+chr(num))
        num +=1
        count +=1
#If it is a lowercase letter, start a lowercase loop
if 96<num and num<123:
    count = 0
    while num<123:
        print(count*' '+chr(num))
        num +=1
        count +=1
