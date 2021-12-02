#

country = input("please enter a country ")

# accesing string by its index

print("first 'char' in country", country, ", country[0] = ", country[0])

# if index in negative, it starts counting from the end to the beginning
print("last 'char' in country", country, ", country[", len(country) -1, "] = ", country[len(country) - 1 ])
