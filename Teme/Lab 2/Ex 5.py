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