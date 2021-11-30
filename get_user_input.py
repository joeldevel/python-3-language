
# input returns a string, so if we want a number we must cast input into a number
user_input = input("Please type something ")

print("You've typed ", user_input)

user_numeric_input = float(input("Now please enter a number "))

print("You've entered", str(user_numeric_input))

print( "*" * 6, "End of program", "*" * 6)
