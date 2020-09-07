from re import match
string = input("enter url  ")

is_valid = match(r'^http(s){0,1}:',string)

print("is valid url ",bool(is_valid))


