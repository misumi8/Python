def extractNumberFromString(string):
    number = ""
    numberFound = False
    for i in string:
        if(i in "1234567890"):
            number = number + i
            numberFound = True
        elif(numberFound):
            break
    return int(number)

print(extractNumberFromString("abc123321abc444"))