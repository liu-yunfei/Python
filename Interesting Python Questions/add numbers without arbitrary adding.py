#Written by Yunfei LIU
#Last update Oct 22, 2020
#This function create a dictionary which represent a sum table of two unit digits
#The key of dictionary are tuple and the value is a tuple of the two digits
#For example, the value of key (5,9) is (1,5)
def table():
    table = dict()
    for i in range(10):
        for j in range(10):
            table[(i,j)] = ((i+j)//10,(i+j)-((i+j)//10)*10)
    return table
#Now run the table function to create a dictionary
dictionary = table()

#This function add up two unit digits. 
#It receives a list with 2 unit digits and return a list of digits of sum
def add2small(number):
    x = number[0]
    y = number[1]
    global dictionary
    s = dictionary[(x,y)]
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
        S = add2large(S,int(L[j]))
    return S

#Main function
def main(list):
    print('Input list '+str(list))
    print('The sum is '+str(addmany(list)))