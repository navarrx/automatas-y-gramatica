
afn = {
    'q0': {'a': ['q1'], 'ε': ['qf']},
    'q1': {'a': ['q2'], 'b': ['qf']},
    'q2': {'a': ['q1'], 'b': ['qf']},
    'qf': {'a': ['qf'], 'bb': ['qf']}
}
def simular_afn(afn, estado_actual, cadena):
    if cadena == '':
        return estado_actual in afn['qf']
    elif estado_actual in afn:
        transiciones = afn[estado_actual]
        if 'ε' in transiciones:
            for estado_siguiente in transiciones['ε']:
                if simular_afn(afn, estado_siguiente, cadena):
                    return True
        if cadena[0] in transiciones:
            for estado_siguiente in transiciones[cadena[0]]:
                if simular_afn(afn, estado_siguiente, cadena[1:]):
                    return True
    return False
cadena = 'aabaab'
if simular_afn(afn, 'q0', cadena):
    print(f'La cadena "{cadena}" es aceptada por el AFN.')
else:
    print(f'La cadena "{cadena}" no es aceptada por el AFN.')
