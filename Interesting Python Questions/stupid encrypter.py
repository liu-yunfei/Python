"""This function is used to verify key.
If the key is valid, return a dictionary with key and answer
If the key is invalid, return False """
def isvalid(Key):
    #Check the length of string first
    if len(Key) != 26:
        return False
    #Use a dictionary to store the key and value
    d = dict()
    Char = 'a'
    for i in Key:
        #Check whether the char is alphabet or already in dictionary
        if (i in d) or ord(i)<97 or ord(i)>122:
            return False
        else:
            d[i] = Char
            Char = chr(ord(Char)+1)
    #Inverse it for faster searching
    Inv = dict()
    for j in d:
        val = d[j]
        Inv[val] = j
    return Inv

#Main function
def main():
    Dictionary = dict()
    #Get the input and verify it
    while True:
        Key = input('Please enter a key: ')
        if isvalid(Key) != False:
            Dictionary = isvalid(Key)
            break
    String = input('Please enter a string to be encrypted: ')
    EncryptedList = []
    #Search the dictionary to encrypt
    for i in String:
        EncryptedList.append(Dictionary.get(i))
    print(''.join(EncryptedList))

main()
