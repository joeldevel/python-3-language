# A dictionary is a key-value pair structure
#    key   |   value
#   a      |   First letter of the alphabet
#   strada |   street
# and so on

# note: each cat is a dictionary too
# the key is his/her name, the value is another dictionary

cats = { 
        'urga': {'name': 'urga', 'age': 234},
        'poti': {'name': 'poti', 'age': 1233},
        'flon': {'name': 'floncho', 'age': 1456}
        }

user_in = input('which cat do you want to look for? ')

if user_in in cats:
    print(cats[user_in])
else:
    print('cat not found, sorry')
