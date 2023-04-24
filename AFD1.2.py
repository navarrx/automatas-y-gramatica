
alphabet = {'0', '1'}
states = {'q0', 'q1'}
initial_state = 'q0'
accepting_states = {'q1'}
transitions = {
    ('q0', '0'): 'q0',
    ('q0', '1'): 'q1',
    ('q1', '0'): 'q0',
    ('q1', '1'): 'q1'
}
def accept(word):
    current_state = initial_state
    for symbol in word:
        current_state = transitions.get((current_state, symbol))
        if current_state is None:
            return False
    return current_state in accepting_states and word[-1] == '1'


print(accept('000'))
print(accept('104'))
print(accept('1111'))
