
string = input("Inserte una frase o palabra:")

def validate_string(string):
    print(string.isalnum())
    print(len(string) > 0)
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

validate_string(string)
