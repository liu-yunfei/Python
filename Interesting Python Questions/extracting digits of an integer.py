string = str(input("Enter a positive integer:"))
length = len(string)
ans = int(string[length-1])
for i in range(length-1):
    ans -= int(string[i])
print(ans)

