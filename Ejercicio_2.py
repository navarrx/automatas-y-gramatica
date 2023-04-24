def solve(string):
    numeros = string.split()
    print(numeros)
    resultado_parcial = 0
    operacion = None
    total = 0
    for i in range(0, len(numeros)):
        if i % 2 == 0:
            numero = int(numeros[i])
            if operacion == '*':
                resultado_parcial *= numero
            else:
                resultado_parcial = numero
        else:
            operacion = numeros[i]
            if operacion == '+':
                total += resultado_parcial
    total += resultado_parcial
    return total

operacion = "2 * 2 * 2 + 32 * 2"
resultado = solve(operacion)
print(resultado)