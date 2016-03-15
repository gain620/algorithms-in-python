# conventional way
def listSum(numList):
    theSum = 0

    for i in numList:
        theSum += i

    return theSum


# calculating the sum of list using a recursive function
def listSumRecursion(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listSumRecursion(numList[1:])


print('without using recursion ->', listSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

print('using recursion ->', listSumRecursion([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
