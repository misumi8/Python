# 7 -----------------------------------

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

def getCountAndGreatestPalindrome(nums):
    count = 0
    greatest = -1
    for num in nums:
        if(isPalindrome(num)):
            count += 1
            if(num > greatest):
                greatest = num
    if(count == 0):
        return (count, "None")
    return (count, greatest)

print(getCountAndGreatestPalindrome([80, 746, 101, 111, 110, 131, 141]))
