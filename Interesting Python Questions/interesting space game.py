
#This function generate a random tuple from (0,0) to (9,9)
def randomPosition():
    import random
    xPosition = random.randint(0,9)
    yPosition = random.randint(0,9)
    xyPosition = (xPosition,yPosition)
    return xyPosition

#This function verifies whether a component is in a list
def isInList(component,list):
    for i in list:
        if component == i:
            return True
    return False

#This function is used to print the positions
def printPosition(alpha,star):
    countx = 0
    county = 0
    for i in range(11):
        for j in range(11):
            if i == 0 and j != 0:
                print(j-1,end = ' ')
            elif j == 0 and i != 0:
                print(i-1,end = ' ')
            elif (i-1,j-1) == alpha:
                print('x',end = ' ')
            elif isInList((i-1,j-1),star):
                print('*',end = ' ')
            else:
                print(' ',end = ' ')
        print('',end = '\n')

#This function can move Alpha, return the new position of Alpha
def moveAlpha(direction,alpha):
    if direction != 'N' and direction != 'E' and direction != 'S' and direction != 'W':
        return alpha
    if direction == 'W' and alpha[1] != 0:
        newAlpha = (alpha[0],alpha[1]-1)
    elif direction == 'S' and alpha[0] != 9:
        newAlpha = (alpha[0]+1,alpha[1])
    elif direction == "E" and alpha[1] != 9:
        newAlpha = (alpha[0],alpha[1]+1)
    elif direction == "N" and alpha[0] != 0:
        newAlpha = (alpha[0]-1,alpha[1])
    else:
        newAlpha = alpha
    return newAlpha

#This function verify if alpha crashed, return True if crash, False if not
def ifCrash(alpha,star):
    for i in star:
        if i == alpha:
            return True
    return False

#Main function
def main():
    alpha = randomPosition()
    count = 0
    starPosition = []
    while count < 8:
        star = randomPosition()
        if isInList(star,starPosition) or star == alpha:
            continue
        starPosition.append(star)
        count += 1
    while True:
        printPosition(alpha,starPosition)
        direction = input("Please enter the direction (N, E, S or W):")
        alpha = moveAlpha(direction,alpha)
        if ifCrash(alpha,starPosition):
            starPosition.remove(alpha)
            alpha = (-1,-1)
            printPosition(alpha,starPosition)
            print("Alpha crashes!")
            return 0


main()