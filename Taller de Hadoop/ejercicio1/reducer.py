#!/usr/bin/env python

from operator import itemgetter
import sys

# inicializamos variables
current_word = None
current_count = 0
word = None

# input viene del STDIN (que a su vez es el outup que sale del mapper.py)
for line in sys.stdin:
    # remover espacios en blanco al inicio y fin de la linea
    line = line.strip()

    # parsear el par clave-valor que viene del mapper.py
    word, count = line.split('\t', 1)

    # count podria no ser un string, convertimos en int y en cualquier otro caso lo ignoramos
    try:
        count = int(count)
    except ValueError:
        # si no es int se ignora la linea
        continue

    # este IF-switch solo funciona porque Hadoop ordena el output del mapper.py
    # por la clave (aqui: word) antes que sea pasado al reducer.py
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # imprimir el resultado al STDOUT
            print '%s\t%s' % (current_word, current_count)
        current_count = count
        current_word = word

# Imprimir la ultima linea si es necesario
if current_word == word:
    print '%s\t%s' % (current_word, current_count)
