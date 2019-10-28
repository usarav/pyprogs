# If number is divisible by 3 fizz, if number is divisible by 5 buzz,
# if number is divisible by 3 and 5 fizz buzz, else print input


def fizz_buzz(input):
    if int((input % 3 == 0)) and int((input % 5 == 0)):
        return "fizzbuzz"
    if int((input % 3 == 0)):
        return "fizz"
    if int((input % 5 == 0)):
        return "buzz"
    return input

num = int(input("Enter a number:"))
print(num)
print("Entered number is :", fizz_buzz(num))
