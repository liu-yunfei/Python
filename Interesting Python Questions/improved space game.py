"""
The program saves the data in three parts
part1: alpha position, showed as a 2d coordinate
part2: stars position, showed as a list of 8 2d coordinates
part3: the direction of alpha, showed as a number from 0 to 3, reprsents 4 different directions

This file contains all variables in this game, and with this data, we can resume the game.
"""
#This function is used to save the current situation
def save(alpha,starPosition,direction):
    file = open('gamesave.txt','w',encoding = 'UTF-8')
    file.write(str(alpha)+'\n')
    file.write(str(starPosition)+'\n')
    file.write(str(direction)+'\n')
    file.close()

#This function generates a random tuple from (0,0) to (9,9)
def randomPosition():
    import random
    xPosition = random.randint(0,9)
    yPosition = random.randint(0,9)
    xyPosition = (xPosition,yPosition)
    return xyPosition

#This function generates a number from 0 to 3 represents 4 directions
def randomChar():
    import random
    direction = random.randint(0,3)
    return direction
    

#This function set position of alpha
def setPosition(direction): 
    if direction == 0:
        return '^'
    elif direction == 1:
        return '<'
    elif direction == 2:
        return 'v'
    elif direction == 3:
        return '>'

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
                print(setPosition(main.direction),end = ' ')
            elif isInList((i-1,j-1),star):
                print('*',end = ' ')
            else:
                print(' ',end = ' ')
        print('',end = '\n')

#This function can move Alpha, return the new position of Alpha
def moveAlpha(direction,alpha):
    if direction != 0 and direction != 1 and direction != 2 and direction != 3:
        return alpha
    if direction == 1 and alpha[1] != 0:
        newAlpha = (alpha[0],alpha[1]-1)
    elif direction == 2 and alpha[0] != 9:
        newAlpha = (alpha[0]+1,alpha[1])
    elif direction == 3 and alpha[1] != 9:
        newAlpha = (alpha[0],alpha[1]+1)
    elif direction == 0 and alpha[0] != 0:
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
    #Get initial direction and position
    main.direction = randomChar()
    alpha = randomPosition()
    count = 0
    starPosition = []
    while count < 8:
        star = randomPosition()
        if isInList(star,starPosition) or star == alpha:
            continue
        starPosition.append(star)
        count += 1
    #Start moving
    while True:
        printPosition(alpha,starPosition)
        print('Move forward (M)\nTurn left by 90 degrees (L)\nTurn right by 90 degrees (R)\nSave the map (S)')
        command = input("Please enter your command: ")
        #Get user's command
        if command == 'M':
            alpha = moveAlpha(main.direction,alpha)
        elif command == 'L':
            #Change the direction
            if main.direction == 3:
                main.direction = 0
            else:
                main.direction += 1
        elif command == 'R':
            if main.direction == 0:
                main.direction = 3
            else:
                main.direction -= 1
        elif command == 'S':
            #Save the game
            save(alpha,starPosition,main.direction)
            print("Game saved in gamesave.txt!")

        #Verify if alpha crashes
        if ifCrash(alpha,starPosition):
            starPosition.remove(alpha)
            alpha = (-1,-1)
            printPosition(alpha,starPosition)
            print("Alpha crashes!")
            return 0


main()
