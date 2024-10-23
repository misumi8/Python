# 6 ------------------------------------------------

def getCountOfUniqueAndDuplicate(nums):
    uniqueNums = set(nums)
    return len(uniqueNums), len(nums) - len(uniqueNums)

# print(getCountOfUniqueAndDuplicate([1,2,1,2,1,1,3,2,2,3,3,4,4,5,6,6,5]))