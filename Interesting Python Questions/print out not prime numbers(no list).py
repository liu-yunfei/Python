limit = int(input("Please enter an integer: "))
testnumber = 3
count = 1
for i in range(limit-2):
    trialnumber = 2
    while testnumber > trialnumber:
        if testnumber%trialnumber == 0:
            count += 1
            break
        trialnumber += 1
    testnumber += 1
testnumber = 3
count -= 1
print(' '*count+'1')
count -= 1
for j in range(limit-2):
    trialnumber = 2
    while testnumber > trialnumber:
        if testnumber%trialnumber == 0:
            print(' '*count+str(testnumber))
            count -= 1
            break
        trialnumber += 1
    testnumber += 1
