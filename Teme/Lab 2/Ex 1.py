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
