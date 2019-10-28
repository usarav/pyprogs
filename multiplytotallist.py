#a. Multiply numbers in a list
def multiply(*list):
    total = 1
    for number in list:
        total *= number
    return total


print("Multiplied elements total of 2,3,4,5,6,7 is :", multiply(2, 3, 4, 5, 6, 7))

##################################################################################
#b. Multiply given numbers as input in a list

input_string = input("Enter a list element separated by space ")
list = input_string.split() #takes input and splits
print("Calculating multiplied values of elements of input list")
total = 1
for num in list:
    total *= int(num)
print("Total = ", total)

#################################################################################
#c. Function to multiply elements(inputs taken from user) in a list


def multiplyinputs_in_list(*list):
    input_string = input("Enter a list element separated by space")
    list = input_string.split()
    print("Calculating multiplied values of elements of input list")
    total = 1
    for num in list:
        total *= int(num)
        #print("Total = ", total)
    return total


print("Total of Multiplied elements of inputs given :", multiplyinputs_in_list(list))

#################################################################################
