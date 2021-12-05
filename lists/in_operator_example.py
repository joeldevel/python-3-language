# Example of using 'in' to check username and password -- Do not use it in real life scenario!
db = [
        ['john',    'abc'],
        ['urga',    '123'],
        ['poti',    'xyz'],
        ['floncho', 'pbs']
    ]

print("~~~ Login page ~~~")
username = input("Your username: ")
password = input("Your password ")

if [username, password] in db :
    print("Welcome back", username, "!")
else:
    print("XXX Access denied XXX")
