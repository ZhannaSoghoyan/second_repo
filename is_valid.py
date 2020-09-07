from re import match
string = input("enter url  ")

is_valid = match(r'^http(s){0,1}[:]{1}[/]{2}[w]{3}[\.]{1}[\w]{1,}[\.]{1}[a-z]{3}',string)

print("is valid url ",bool(is_valid))


