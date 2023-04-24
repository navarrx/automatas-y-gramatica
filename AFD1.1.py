def evaluate(string):
    state = 1
    for char in string:
        if state == 1:
            if char == 'a' or char == 'b':
                state = 1
            else:
                return False
    return True

string = input("Ingrese una cadena: ")
if evaluate(string):
    print("La cadena es válida")
else:
    print("La cadena no es válida")

