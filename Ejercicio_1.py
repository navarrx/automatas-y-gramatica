

def validate_string(string):
    print(string.isalnum())
    if any(i.isalpha() for i in string):
        print(True)
    else:
        print(False)
    if any(i.isupper() for i in string):
        print(True)
    else:
        print(False)
    if any(i.islower() for i in string):
        print(True)
    else:
        print(False)
    if any(i.isdigit() for i in string):
        print(True)
    else:
        print(False)
    print(len(string) >= 8)

string = input("xy@z")
validate_string(string)