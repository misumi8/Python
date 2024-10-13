# 1 --------------------------------

def decToBin(num):
    binForm = ""
    while(num > 0):
        # print(num, num % 2)
        if(num % 2 == 1):
            binForm += "1"
        else:
            binForm += "0"
        num = num // 2
    return "0b" + binForm[::-1]

# print(decToBin(110))

# 2 --------------------------------

def binToHex(binNum):
    chars = "ABCDEF"
    hexForm = ""
    i = 0
    count = 0
    decNum = 0
    while(binNum > 0):
        if(binNum % 10 == 1):
            decNum += pow(2, i)
        count += 1
        i += 1
        binNum = binNum // 10
        if(count == 4 or binNum == 0):
            if(decNum > 9):
                hexForm = chars[decNum % 10] + hexForm
            else:
                hexForm = str(decNum) + hexForm
            count = 0
            decNum = 0
            i = 0
    return "0x" + hexForm

# print("binToHex", binToHex(101010111011101111011101000001111))

# 3 --------------------------------

def decToAny(string, num):
    uniqueChars = set()
    for i in string:
        if(i in uniqueChars):
            return "First parameter must contain unique characters only"
        else:
            uniqueChars.add(i)
    convertedForm = ""
    baseToConvert = len(string)
    while(num > 0):
        convertedForm = string[num % baseToConvert] + convertedForm
        num = num // baseToConvert
    return convertedForm

# print(decToAny("abcd", 301))

# 4 --------------------------------

def decToHex(numDec):
    hexForm = ""
    chars = "ABCDEF"
    while(numDec > 0):
        dec = numDec % 16
        numDec = numDec // 16
        if(dec > 9):
            hexForm += chars[dec%10]
        else:
            hexForm += str(dec)
    return "0x" + hexForm[::-1]

# print(decToHex(120545415617)) # 1C111111C1

# 5 --------------------------------

def testBrackets(string):
    brackets = []
    for i in string:
        if(i == '('):
            brackets.append('(')
        elif(i == ')'):
            if(len(brackets) and brackets[-1] == '('):
                brackets.pop()
            else:
                return False;
    return len(brackets) == 0

# print(testBrackets("8-4*(3+7/8+4/(5-9)"))

# 6 --------------------------------

def hexOfAscii(string):
    finalForm = ""
    for i in string:
        if(i == " "):
            finalForm += "\n"
        else:
            hexForm = ""
            asciiCode = ord(i)
            chars = "ABCDEF"
            while (asciiCode > 0):
                dec = asciiCode % 16
                asciiCode = asciiCode // 16
                if (dec > 9):
                    hexForm = chars[dec % 10] + hexForm
                else:
                    hexForm = str(dec) + hexForm
            finalForm += hexForm
    return finalForm

# print(hexOfAscii("abc 012"))

# 7 --------------------------------

def getNumOfUpper(string):
    count = 0
    for i in string:
        if(i.isupper()):
            count += 1
    return count

# print(getNumOfUpper("A fost, de asemenea, Remarcabil pentru Razboaiele persane si Pentru razboaiele Dintre orasele-state Grecesti."))

# 8 (transferred to probleme complicate) --------------------------------

# 9 --------------------------------

def getFirstAndLastChars(string):
    firstAndLastChars = ""
    words = string.split(" ")
    for i in words:
        i = i.strip(",")
        i = i.strip(".")
        firstAndLastChars += i[0] + i[-1] + ' '
    return firstAndLastChars

# print(getFirstAndLastChars("A fost, de asemenea, Remarcabil pentru Razboaiele persane si Pentru razboaiele Dintre orasele-state Grecesti."))

# 10 --------------------------------

def getInversedWords(string):
    words = string.split(" ")
    resultString = ""
    for word in words:
        resultString += word[::-1] + " "
    return resultString

# print(getInversedWords("Propozitia data este formata din sapte cuvinte"))

# 11 --------------------------------

def getCountVowelsAndConsonants(string):
    vowels = 0
    consonants = 0
    for i in string:
        if(i.lower() in "aeiou"):
            vowels += 1
        elif(i.lower() in "bcdfghjklmnpqrstvwxyz"):
            consonants += 1
    return "Vowels: " + str(vowels) + " || Consonants: " + str(consonants)

# print(getCountVowelsAndConsonants("7aaaaIaa|5bCCCd"))

# 12 --------------------------------

def isPalindrome(number):
    reversed = 0
    numberCpy = number
    numberCpy2 = number
    step = 1
    while(numberCpy > 0):
        numberCpy = numberCpy // 10
        step = step * 10
    step = step // 10
    while(number > 0):
        reversed = reversed + ((number % 10) * step)
        number = number // 10
        step = step // 10
    return reversed == numberCpy2

# print(isPalindrome(12321))
# print(isPalindrome(122321))