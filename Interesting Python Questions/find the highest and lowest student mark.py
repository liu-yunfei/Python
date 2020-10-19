numcourse = int(input('Enter the number of courses: '))
highest = 0
lowest = 100
for i in range(numcourse):
    numstudent = int(input('Enter no of students taken course '+str(i+1)+':'))
    mark = 0
    count = 0
    for j in range(numstudent):
        studentmark = int(input("Enter Student "+str(j+1)+"'s mark: "))
        mark += studentmark
        if highest <= studentmark:
            highest = studentmark
        if lowest >= studentmark:
            lowest = studentmark
        count += 1
    print("Average Mark: "+str(mark/count))
print('The highest mark is '+str(highest))
print('The lowest mark is '+str(lowest))
