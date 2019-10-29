def add_inputs_in_list(*list):


    input_string = input("Enter a list element separated by space")
    list = input_string.split()
    print("Calculating sum of values of elements of input list")
    total = 1
    for num in list:
        total += int(num)
    return total


print("Total sum of input given :", add_inputs_in_list(list))