import re
from collections import Counter
texto = "¿Qué sabemos sobre un autómata que puede aceptar este lenguaje L? En primer lugar, sabemos que su alfabeto de entrada es Σ = {0,1}. Tiene un determinado conjunto de estados, Q, siendo uno de ellos, por ejemplo q0, el estado inicial. Este autómata tiene que recordar las entradas que ha leído hasta el momento. Para decidir si 01 es una subcadena de la entrada, A tiene que recordar: 1. ¿Ha leído ya una subcadena 01? En caso afirmativo, aceptará cualquier secuencia de entradas futura; es decir, sólo se encontrará en estados de aceptación. 2. ¿Todavía no ha leído la secuencia 01, pero la entrada más reciente ha sido un 0, de manera que si ahora lee un 1, habrá leído la subcadena 01 y podrá aceptar cualquier cosa que lea de ahí en adelante? 3. ¿Todavía no ha leído la secuencia 01, pero la última entrada no existe (acaba de iniciarse) o ha sido un 1? En este caso, A no puede aceptar la entrada hasta que no lea un 0 seguido inmediatamente de un 1. Cada una de estas tres condiciones puede representarse mediante un estado. La condición (3) se representa mediante el estado inicial, q0. Nada más comenzar seguramente necesitaremos leer un 0 seguido de un 1. Pero si estando en el estado q0 lo primero que leemos es un 1, entonces no leeremos la secuencia 01 y, por tanto, deberemos permanecer en el estado q0. Es decir, δ (q0,1) = q0. Sin embargo, si estamos en el estado q0 y a continuación leemos un 0, nos encontraremos en el caso de la condición (2). Es decir, nunca leeremos la secuencia 01, pero tenemos un 0. Por tanto, utilizaremos q2 para representar la condición (2). La transición de q0 para la entrada 0 es δ (q0,0) = q2. Consideremos ahora las transiciones desde el estado q2. Si leemos un 0, no mejoramos nuestra situación pero tampoco la empeoramos. No hemos leído la secuencia 01, pero 0 ha sido el último símbolo, por lo que quedamos a la espera de un 1. El estado q2 describe esta situación perfectamente, por lo que deseamos que δ (q2,0) = q2. Si nos encontramos en el estado q2 y leemos una entrada 1, entonces disponemos de un 0 seguido de un 1. Ahora podemos pasar a un estado de aceptación, que denominaremos q1, y que se corresponde con la condición (1). Es decir, δ (q2,1) = q1. Por último, tenemos que diseñar las transiciones para el estado q1. En este estado, ya hemos leido una secuencia 01, así que, independientemente de lo que ocurra, nos encontraremos en una situación en la que hemos leído la secuencia 01. Es decir, δ (q1,0) =δ (q1,1) = q1."
word_regex = r'\b[a-zA-Z]+\b'
palabras = re.findall(word_regex, texto)


def word_evaluator():
    word_counter = Counter(palabras)
    most_repeated_word = word_counter.most_common(1)[0]
    print("The most repeated word is: "+most_repeated_word[0])
    print("The word is repeated "+str(most_repeated_word[1])+" times")


word_evaluator()
