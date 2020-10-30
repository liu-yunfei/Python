#This function receive two names in string and transform it into the answer string
def transform_name(FirstName,LastName,Char):
    FullNameStr = FirstName + ' ' + LastName
    FullNameList = []
    #Because the string is immutable, transform it into list
    for j in FullNameStr:
        FullNameList.append(j)
    count = 0
    #Letter is replaced by Char
    for i in FullNameList:
        if count%2 == 0 and i != ' ':
            FullNameList[count] = Char
        count += 1
    #Transform back and return the answer string
    FullNameStr = ''.join(FullNameList)
    return FullNameStr

#This function receive a string and output it like a triangle
def print_name(AnsStr):
    count = 1
    #Print the previous half
    for i in AnsStr:
        print(AnsStr[:count])
        count += 1
    #Print the following part
    count -= 1
    for j in AnsStr:
        count -= 1
        print(AnsStr[:count])

#Main function
def main():
    First = input('Please input your first name: ')
    Last = input('Please input your last name: ')
    Symbol = input('Please input a symbol: ')
    print_name(transform_name(First,Last,Symbol))
main()