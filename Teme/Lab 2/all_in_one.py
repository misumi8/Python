def gcdMultipleNum(*nums):
    gcd = 1
    for cd in range(1, min(nums)+1):
        index = 0
        for num in nums:
            if(num % cd == 0):
                if(num is nums[-1]):
                    gcd = cd
                    break
            else:
                break
    return gcd

print(gcdMultipleNum(75,150,750,100,825,25))

# -------------------------------------

def vowelsCount(str):
    vowels = 0
    for i in str:
        if(i in "aeiouAEIOU"):
            vowels = vowels + 1
    return vowels

print(vowelsCount("5vowelsInThisWord"))

# -------------------------------------

def occurNum(firstStr, secondStr):
    return secondStr.count(firstStr)

print(occurNum("abc", "abcAaacabcAabcAaaaabcA"))

# -------------------------------------

def UpCamelToLowUnder(upperCamelString):
    for char in upperCamelString:
        if(char.isupper()):
            upperCamelString = upperCamelString.replace(char, "_" + char.lower());
    return upperCamelString

print(UpCamelToLowUnder("upperCamelStringTest"))

# -------------------------------------

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

print(isPalindrome(12321))

# -------------------------------------

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

# -------------------------------------

def countBits(number):
    return bin(number).count("1")

print(countBits(111)) # 1101111 = 6

# -------------------------------------

def getWordsCount(str):
    words = 0
    for i in str:
        if(i == " "):
            words = words + 1
    if(len(str) > 0):
        words = words + 1
    return words

# Another possible solution:
# def getWordsCount(str):
#     if(len(str) > 0):
#         return len(str.split(" "))
#     else:
#         return 0

print(getWordsCount("I have Python exam"))