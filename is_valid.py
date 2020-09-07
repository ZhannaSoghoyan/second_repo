from re import match
string = input("enter url  ")

is_valid = match(r'^http:',string)

print("is valid url ",bool(is_valid))


