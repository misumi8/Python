# 2 -----------------------------------

def isPrime(num):
    if(num < 2):
        return False
    for i in range(2, num // 2 + 1):
        if(num % i == 0):
            return False
    return True

def findPrimeNumbers(list):
    newList = []
    for i in list:
        if(isPrime(i)):
            newList.append(i)
    return newList

newList = findPrimeNumbers([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])
for i in newList:
    print(i)