﻿# Written by Yunfei LIU
# Oct 8, 2020
# Please obey the license GPLv3

InputStr = str(input())
CharList = []
j = 0
for i in InputStr:
    CharList.append(i)
    CharList[j] = bin(ord(CharList[j])).replace('0b','')
    CharList[j] = '0'*(8-len(CharList[j])) + CharList[j]
    j += 1
OutputStr = ''.join(CharList)
print(int(OutputStr,2))
