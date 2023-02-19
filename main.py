def main():

    # get number of cases
    caseNo = int(input())
    sums = []
    sums = (caseRecurse(caseNo, sums))
    printSums(caseNo, sums, 0)


def caseRecurse(caseNo, sumList):
    if (caseNo == 0):
        return sumList

    # get number of integers
    integerNo = int(input())

    # parse by removing " "'s
    numbers = input().split()

    # recurse through numbers list and add to sums list
    sum = (squareSum(integerNo - 1, numbers, 0))
    sumList.append(sum)

    return (caseRecurse(caseNo - 1, sumList))


def squareSum(integerNo, numbers, currentSum):
    if (integerNo < 0):
        return currentSum

    elif (int(numbers[integerNo]) >= 0):  # check if positive
        # square, add to running total
        currentSum += int(numbers[integerNo]) ** 2
        return squareSum(integerNo - 1, numbers, currentSum)

    else:
        return squareSum(integerNo - 1, numbers, currentSum)

# must print recursively to match output example


def printSums(caseNo, sumList, counter):
    if (counter == caseNo):
        return
    else:
        print(sumList[counter])
        return printSums(caseNo, sumList, counter + 1)


if __name__ == "__main__":
    main()
