# Curso BigData & Data Analytics by Handytec
# Fecha: Mayo-2016
# Descripcion: Programa que grafica el sin(x)

import numpy
from matplotlib import pyplot

Calcular valores de los ejes
x = numpy.linspace(0, 2 * numpy.pi, 100)
y = numpy.sin(x)

# Dibujar el grafico
pyplot.plot(x, y)
pyplot.show()