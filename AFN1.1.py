def evaluate():
    string = input("Ingrese una cadena: ")
    text = list(string)
    print(text)
    i = 0
    if len(text) == 0:
        return True
    for i in range(len(text)):
        if text[i] == "a" or text[i] == "b":
            i = i+1
            if i == len(text):
                return True
        else:
            return False
print(evaluate())

