#This function is used for clean input
def cleanup(string):
    newStr = ''
    #Only detect useful char in the input
    for char in string:
        if char == '|' or char == 'M' or char == 'C' or char == 'G' or char == 'W':
            newStr += char
        #Transform lowercase to uppercase
        if char == 'm' or char == 'c' or char == 'g' or char == 'w':
            newStr += chr(ord(char)-32)
    ansList = []
    #Separate it to list
    for i in range(len(newStr)//5):
        ansList.append(newStr[:5])
        if len(newStr)>5:
            newStr = newStr[5:]
    return ansList

#This function is used for verify the situation and operation
def check(list):
    verify = True
    #Check the initial and end status
    if list[0][0] != '|':
        print('Start state %s is incorrect' %list[0])
        verify = False
    if not islegal(list[0]):
        print('The state %s is illegal' % list[0])
    if list[len(list)-1][4] != '|':
        print('End state %s is incorrect' %list[len(list)-1])
        verify = False
    #Check the move and the status
    for i in range(len(list)-1):
        if not islegal(list[i+1]):
            print('The state %s is illegal' % list[i+1])
            verify = False
        if not canmove(list[i],list[i+1]):
            print('The move %s -> %s is not allowed' %(list[i],list[i+1]))
            verify = False
    return verify

#Main function
def main(solList):
    for item in solList:
        print('Imput solution: %s' %item)
        verify = check(cleanup(item))
        if verify == False:
            print("Input solution is incorrect")
        if verify == True:
            print("Input solution is correct\nThe solution:")
            printSol(cleanup(item))

#This function print a solution
def printSol(list):
    for i in range(len(list)-1):
        previous = list[i]
        now = list[i+1]
        priver = previous.index('|')
        nriver = now.index('|')
        pwest = previous[:priver]
        peast = previous[priver+1:]
        nwest = now[:nriver]
        neast = now[nriver+1:]
        #Check whether the man brings object
        #The man not brings anything
        if abs(len(pwest)-len(nwest)) == 1:
            if len(pwest)-len(nwest) == 1:
                print('man to East')
            else:
                print('man to West')
            continue
        #Ths man brings something
        if abs(len(pwest)-len(nwest)) == 2:
            bring = ''
            #Check the direction
            if (len(pwest)-len(nwest)) == 2:
                direction = 'East'
                #Check the object he brings
                if ('W' in pwest) and ('W' in neast):
                    bring = 'wolf'
                elif ('C' in pwest) and ('C' in neast):
                    bring = 'cabbage'
                else:
                    bring = 'goat'
            else:
                direction = 'West'
                if ('W' in peast) and ('W' in nwest):
                    bring = 'wolf'
                elif ('C' in peast) and ('C' in nwest):
                    bring = 'cabbage'
                else:
                    bring = 'goat'
            print("man and %s to %s"%(bring,direction))
            
        
#This function is used for check situation is legal
def islegal(string):
    river = string.index('|')
    west = string[:river]
    east = string[river+1:]
    #Check whether cabbage and goat are in the same side without man
    if ((('C' in east) and ('G' in east) and ('M' not in east)) or (('C' in west) and ('G' in west) and ('M' not in west))):
        return False
    #Check whether wolf and goat are in the same side without man
    if ((('W' in east) and ('G' in east) and ('M' not in east)) or (('W' in west) and ('G' in west) and ('M' not in west))):
        return False
    return True

#This function is used for check operation is valid
def canmove(previous,now):
    priver = previous.index('|')
    nriver = now.index('|')
    pwest = previous[:priver]
    peast = previous[priver+1:]
    nwest = now[:nriver]
    neast = now[nriver+1:]
    #If 3 objects move one time, wrong
    if abs(len(pwest)-len(nwest)) > 2:
        return False
    #If man is not driving the boat, wrong
    if (('M' in pwest) and ('M' in nwest)) or (('M' in peast) and ('M' in neast)):
        return False
    return True


