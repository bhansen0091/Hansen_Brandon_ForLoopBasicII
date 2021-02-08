# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

testList = [-1, 3, 5, -5]
def biggieSize(paramList):
    for i in range(0,len(paramList)):
        if paramList[i] > 0:
            paramList[i] = "big"
    return paramList
print(biggieSize(testList))


# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

testList = [-1,1,1,1]
testList2 = [1,6,-4,-2,-7,-2]
def countPos(paramList):
    count = 0
    for i in range(0,len(paramList)):
        if paramList[i] > 0:
            count += 1
    paramList[len(paramList)-1] = count
    return paramList
print(countPos(testList))
print(countPos(testList2))

# Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

testList = [1,2,3,4]
testList2 = [6,3,-2]
def sumTotal(paramList):
    sum = 0
    for i in range(len(paramList)):
        sum += paramList[i]
    return sum
print(sumTotal(testList))
print(sumTotal(testList2))

# Average - Create a function that takes a list and returns the average of all the values.x
# Example: average([1,2,3,4]) should return 2.5

testList = [1,2,3,4]
def average(paramList):
    sum = 0
    avg = 0
    for i in range(len(paramList)):
        sum += paramList[i]
    avg = sum / len(paramList)
    return avg
print(average(testList))

# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

testList = [37,2,1,-9]
testList2 = []
def length(paramList):
    return len(paramList)
print(length(testList))
print(length(testList2))

# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

testList = [37,2,1,-9]
testList2 = []
def minimum(paramList):
    minVal = 0
    if len(paramList) > 0:
        for i in range(len(paramList)):
            if paramList[i] < minVal:
                minVal = paramList[i]
    else:
        return False
    return minVal
print(minimum(testList))
print(minimum(testList2))

# Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

testList = [37,2,1,-9]
testList2 = []
def maximum(paramList):
    maxVal = 0
    if len(paramList) > 0:
        for i in range(len(paramList)):
            if paramList[i] > maxVal:
                maxVal = paramList[i]
    else:
        return False
    return maxVal
print(maximum(testList))
print(maximum(testList2))

# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }



# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]