# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

test_list = [-1, 3, 5, -5]
def biggie_size(param_list):
    for i in range(0,len(param_list)):
        if param_list[i] > 0:
            param_list[i] = "big"
    return param_list
print(biggie_size(test_list))


# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

test_list = [-1,1,1,1]
test_zero = [0,0,1,2,5,-3,-5]
test_list_2 = [1,6,-4,-2,-7,-2]
def count_pos(param_list):
    count = 0
    for i in range(0,len(param_list)):
        if param_list[i] > 0:
            count += 1
    param_list[len(param_list)-1] = count
    return param_list
print(count_pos(test_list))
print(count_pos(test_zero))
print(count_pos(test_list_2))

# Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

test_list = [1,2,3,4]
test_list_2 = [6,3,-2]
def sum_total(param_list):
    sum = 0
    for i in range(len(param_list)):
        sum += param_list[i]
    return sum
print(sum_total(test_list))
print(sum_total(test_list_2))

# Average - Create a function that takes a list and returns the average of all the values.x
# Example: average([1,2,3,4]) should return 2.5

test_list = [1,2,3,4]
def average(param_list):
    sum = 0
    avg = 0
    for i in range(len(param_list)):
        sum += param_list[i]
    avg = sum / len(param_list)
    return avg
print(average(test_list))

# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

test_list = [37,2,1,-9]
test_list_2 = []
def get_length(param_list):
    return len(param_list)
print(get_length(test_list))
print(get_length(test_list_2))

# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

test_list = [37,2,1,-9]
test_list_2 = []
def get_minimum(param_list):
    min_val = 0
    if len(param_list) > 0:
        for i in range(len(param_list)):
            if param_list[i] < min_val:
                min_val = param_list[i]
    else:
        return False
    return min_val
print(get_minimum(test_list))
print(get_minimum(test_list_2))

# Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

test_list = [37,2,1,-9]
test_list_2 = []
def get_maximum(param_list):
    max_val = 0
    if len(param_list) > 0:
        for i in range(len(param_list)):
            if param_list[i] > max_val:
                max_val = param_list[i]
    else:
        return False
    return max_val
print(get_maximum(test_list))
print(get_maximum(test_list_2))

# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

test_list = [37,2,1,-9]
test_list_2 = [1,5,3,87,15,-123]
def ultimate_analysis(param_list):
    new_dictionary = {
        "sum_total" : 0,
        "average"   : 0,
        "minimum"   : 0,
        "maximum"   : 0,
        "length"    : 0
    }
    sum, avg, min_val, max_val, length = 0, 0, 0, 0, len(param_list)
    if param_list != None:
        for i in range(len(param_list)):
            sum += param_list[i]
            if param_list[i] > max_val:
                max_val = param_list[i]
            elif param_list[i] < min_val:
                min_val = param_list[i]
        avg = sum/length
        new_dictionary["sum_total"] = sum
        new_dictionary["average"] = avg
        new_dictionary["minimum"] = min_val
        new_dictionary["maximum"] = max_val
        new_dictionary["length"] = length
    return new_dictionary
new_dict_1 = ultimate_analysis(test_list)
new_dict_2 = ultimate_analysis(test_list_2)
print(new_dict_1)
print(new_dict_2)


# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

test_list = [37,2,1,-9]
test_list_2 = [1,2,3,4,5]
def reverse_list(param_list):
    counter = len(param_list)-1
    for i in range(int(len(param_list) / 2)):
        temp = param_list[i]
        param_list[i] = param_list[counter]
        param_list[counter] = temp
        counter -= 1
    return param_list
print(reverse_list(test_list))
print(reverse_list(test_list_2))