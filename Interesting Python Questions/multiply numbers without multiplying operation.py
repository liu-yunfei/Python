"""
#This part is from A3Q3
#Written by Yunfei LIU
#Last update Oct 22, 2020
"""
#This function create a dictionary which represent a sum table of two unit digits
#The key of dictionary are tuple and the value is a tuple of the two digits
#For example, the value of key (5,9) is (1,5)
def addtable():
    table = dict()
    for i in range(10):
        for j in range(10):
            table[(i,j)] = ((i+j)//10,(i+j)-((i+j)//10)*10)
    return table
#Now run the table function to create a dictionary
adddictionary = addtable()

#This function add up two unit digits. 
#It receives a list with 2 unit digits and return a list of digits of sum
def add2small(number):
    x = number[0]
    y = number[1]
    global adddictionary
    s = adddictionary[(x,y)]
    s10 = s[0]
    s1 = s[1]
    return [s10,s1]

#This function add up three unit digits.
#It receives a list with 3 unit digits and return a list of digits of sum
def add3small(number):
    x,y,c = map(int,number)
    a10,a1 = map(int,add2small([x,y]))
    b10,b1 = map(int,add2small([a1,c]))
    d10,d1 = map(int,add2small([a10,b10]))
    s1 = b1
    s10 = d1
    return [s10,s1]

#This function add up two multi-digits numbers
#It receives 2 multi-digits numbers and return a integer of sum
def add2large(number1,number2):
    #This function receives 2 multi-digit numbers and return 2 lists of this numbers
    def transintolist(mulnumber1,mulnumber2):
        string1 = str(mulnumber1)
        string2 = str(mulnumber2)
        length1 = len(string1)
        length2 = len(string2)
        list1 = []
        list2 = []
        for i in range(length1):
            list1.append(string1[length1-1-i])
        for j in range(length2):
            list2.append(string2[length2-1-j])
        return [list1,list2]
    #Now start the program
    X,Y = map(list,transintolist(number1,number2))
    m = len(X)
    n = len(Y)
    #If the length is different, add 0 to the shorter one to avoid overflow
    if m > n:
        p = m
        for k in range(m-n):
            Y.append(0)
    else:
        p = n
        for l in range(n-m):
            X.append(0)
    C = []
    C.append(0)
    s = []
    for i in range(p):
        a10,a1 = map(int,add3small([X[i],Y[i],C[i]]))
        C.append(a10)
        s.append(a1)
    # list s is in the reversed order, so change it to the correct order
    S = []
    for j in range(len(s)):
        S.append(str(s[len(s)-1-j]))
    AnsList = [str(C[p])]+S
    return int(''.join(AnsList))

#This function add up many multi-digit integers
#It receives a list of multi-digits string and return the sum in integer format
def addmany(L):
    length = len(L)
    S = 0
    for j in range(length):
        S = str(add2large(S,int(L[j])))
    return S


"""
#This part is from A4Q3
#Written by Yunfei LIU
#Last update Nov 3, 2020
"""
#This function create a dictionary which represent a product table of two unit digits
#The key of dictionary are tuple and the value is a tuple of the two digits
#For example, the value of key (5,9) is (4,5)
def multiplytable():
    table = dict()
    for i in range(10):
        for j in range(10):
            table[(i,j)] = ((i*j)//10,(i*j)-((i*j)//10)*10)
    return table
#Now run the table function to create a dictionary
multiplydictionary = multiplytable()
#This function multiplies two unit digits. 
#It receives a list with 2 unit digits and return a list of digits of product
def multiply2small(number):
    x = number[0]
    y = number[1]
    global multiplydictionary
    s = multiplydictionary[(x,y)]
    s10 = s[0]
    s1 = s[1]
    return [s10,s1]

#This function multiplies three unit digits.
#It receives a list with 3 unit digits and return a list of digits of product
def multiply3small(number):
    x,y,c = map(int,number)
    a10,a1 = map(int,multiply2small([x,y]))
    b10,b1 = map(int,multiply2small([a1,c]))
    d100,d10 = map(int,multiply2small([a10,c]))
    s1 = b1
    e = add2small([b10,d10])
    s10 = e[1]
    s100 = add2small([d100,e[0]])[1]
    return [s100,s10,s1]

#This function multiplies two multi-digits numbers
#It receives 2 multi-digits numbers and return a integer of product
def multiply2large(number1,number2):
    #This function receives 2 multi-digit numbers and return 2 lists of this numbers
    def transintolist(mulnumber1,mulnumber2):
        string1 = str(mulnumber1)
        string2 = str(mulnumber2)
        length1 = len(string1)
        length2 = len(string2)
        list1 = []
        list2 = []
        for i in range(length1):
            list1.append(string1[length1-1-i])
        for j in range(length2):
            list2.append(string2[length2-1-j])
        return [list1,list2]
    #Now start the program
    X,Y = map(list,transintolist(number1,number2))
    ansList = []
    #The digits of answer should no longer than the sum of previous digits
    for i in range(len(X)+len(Y)):
        ansList.append([0])
    #Multiply the digits individually and add it to the ansList
    for j in range(len(X)):
        for k in range(len(Y)):
            sum = multiply2small([int(X[j]),int(Y[k])])
            ansList[j+k].append(sum[1])
            ansList[j+k+1].append(sum[0])
    count = 0
    for digit in ansList:
        digitSum = str(addmany(digit))
        ansList[count] = int(digitSum[len(digitSum)-1])
        for m in range(len(digitSum)-1):
            ansList[count+m+1].append(int(digitSum[len(digitSum)-2-m]))
        count += 1
    #Now the list is in reverse order
    revAnsList = []
    for n in range(len(ansList)):
        revAnsList.append(str(ansList[len(ansList)-1-n]))
    return int(''.join(revAnsList))

#This function multiplies many multi-digit integers
#It receives a list of multi-digits string and return the product in integer format
def multiplymany(L):
    length = len(L)
    S = 1
    for j in range(length):
        S = multiply2large(S,int(L[j]))
    return S

#This function change a list of float to a list of integer, just delete the dot
#It receives a float list and return the float position from the right to the left
def floatToInteger(list):
    floatPosition = 0
    listCount = 0
    for item in list:
        count = 0
        for char in str(item):
            if char == '.':
                floatPosition += int(len(item)-count-1)
                list[listCount] = item[:count]+item[count+1:]
                break
            count += 1
        listCount += 1
    return list,floatPosition

#This function is used to add dot
def addDot(integer,floatPosition):
    if floatPosition == 0:
        return integer
    stringInt = str(integer)
    floatNumber = stringInt[:len(stringInt)-floatPosition]+'.'+stringInt[len(stringInt)-floatPosition:]
    return floatNumber

#This function will compare two numbers
def compareFloat(number1, number2):
    dot1 = number1.index('.')
    dot2 = number2.index('.')
    intnumber1 = number1[:dot1]
    intnumber2 = number2[:dot2]
    decnumber1 = number1[dot1+1:]
    decnumber2 = number2[dot2+1:]
    if len(intnumber1) < len(intnumber2):
        intnumber1 = '0'*(len(intnumber2)-len(intnumber1))+intnumber1
    else:
        intnumber2 = '0'*(len(intnumber1)-len(intnumber2))+intnumber2
    if len(decnumber1) < len(decnumber2):
        decnumber1 = decnumber1+'0'*(len(decnumber2)-len(decnumber1))
    else:
        decnumber2 = decnumber2+'0'*(len(decnumber1)-len(decnumber2))
    for i in range(len(intnumber1)):
        if intnumber1[i] > intnumber2[i]:
            return 1
        elif intnumber1[i] < intnumber2[i]:
            return -1
    for j in range(len(decnumber1)):
        if decnumber1[j] < decnumber2[j]:
            return -1
        elif decnumber1[j] > decnumber2[j]:
            return 1
    return 0

def compareNumber(number1,number2):
    print("Comparing %s %s" %(number1,number2))
    try:
        dot1 = number1.index('x')
    except ValueError:
        number1 = number1+".0"
    try:
        dot2 = number2.index('.')
    except ValueError:
        number2 = number2+".0"
    return compareFloat(number1,number2)

#Main function
def main(list):
    print('Input list '+str(list))
    intList,floatPosition = floatToInteger(list)
    intResult = multiplymany(intList)
    floatResult = addDot(intResult,floatPosition)
    print('The product is '+str(floatResult))


