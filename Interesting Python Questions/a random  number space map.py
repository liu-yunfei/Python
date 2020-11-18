"""
In this program, I'll use tuple to store the place, and the format is (x,y). 
x represents row position and y represents column position.
It will use random number from 0-9 to determine the place of star's x and y individually.
After that, the program will verify if the star conflict with the previous star.
If conflict happens, it will give up and try another possible position until all position are found.
The place of Alpha will determined by user input.
The user should input a tuple which each component should be integer between 0 and 9
The program will verify Alpha's position, if it conflicts with stars, ask user to input again
Then, the program continue verify each time of the user's input to make sure Alpha won't conflict with star
"""

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
    printPosition(alpha,starPosition)

main()
