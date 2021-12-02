user_input = input("Please enter some words ")

# str[start index : end index]
length = len(user_input)
print(user_input[0:length//2])
print(user_input[length//2:])

# example 

url = input("Please enter a url e.g. http://www.banana.com ")
#                                    0         11     -4  0
domain = url[11:-4]

print("the domain is:", domain)
