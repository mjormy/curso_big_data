#!/usr/bin/env python

import sys

# input viene del STDIN (standard input)
for line in sys.stdin:
    # remover espacios en blanco al inicio y final de la linea
    line = line.strip()
    # hacer un splite de la linea en palabras
    words = line.split()
    # iterar sobre las palabras creando un par clave-valor
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        print '%s\t%s' % (word, 1)
