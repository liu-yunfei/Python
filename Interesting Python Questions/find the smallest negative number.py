# Written by Yunfei LIU
# Oct 8, 2020
# Please obey the license GPLv3

#Create a list to save the input
NegInt = []
Neg0 = input("Enter a negative integer (1 or 'end' to end): ")
#Verify the input for the first time
import sys
if Neg0=='1' or Neg0=='end':
    print('No input!')
    sys.exit(0)
#Start the input loop and output
while Neg0!='1' and Neg0!="end":
    Neg1 = input("Enter a negative integer (1 or 'end' to end): ")
    #Verify the new input
    if Neg1=='1' or Neg1=='end':
        print('The smallest integer is: ',Neg0)
        sys.exit(0)
    #If the loop continue, let Neg0 to be the smallest
    if int(Neg1)<int(Neg0):
        Neg0 = Neg1
