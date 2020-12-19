def main():
    #Create list to record month name and days in a month
    monthName = ['January','February','March','April','May','June','July','August','September','October','November','December']
    monthDay = [31,29,31,30,31,30,31,31,30,31,30,31]
    while True:
        userInput = input("Please enter a month in its full name or -1 to end: ")
        #Make sure the input is vaild
        try:
            monthIndex = monthName.index(userInput)
        except ValueError:
            if userInput == '-1':
                print('Bye!')
                return 0
            continue
        #Because Jan 1 is Wednesday, so need to add 3 spaces before the first day
        previousDay = 3
        for i in range(monthIndex):
            previousDay += monthDay[i]
        #Calculate what day is the first day of chosen month
        dayLeft = previousDay % 7
        #Set up the date of chosen month list for print 
        currentMonth = []
        for j in range(dayLeft):
            currentMonth.append('    ')
        #According to the different position of date, add different ending
        for k in range(monthDay[monthIndex]):
            #If the day is not Saturday, add space according to the length of date
            if (k+dayLeft+1)%7 != 0:
                if k < 9:
                    currentMonth.append(str(k+1)+'   ')
                else:
                    currentMonth.append(str(k+1)+'  ')
            #If the day is Saturday, start a new line
            else:
                currentMonth.append(str(k+1)+'\n')
        #Print the title
        print("S   M   T   W   T   F   S")
        #Print the month calendar
        for l in currentMonth:
            print(l,end='')
        #Start a new line for next input
        print('')

main()
            
