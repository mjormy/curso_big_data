# Curso BigData & Data Analytics by Handytec
# Fecha: Marzo-2016
# Descripcion: Programa que califica el Sentimiento del texto ingresado en ingles

import tweet_classifier.classifier as classifier #importamos libreria que analiza sentimiento en textos en ingles

text = classifier.doSentimentAnalysis(raw_input('Ingrese texto en Ingles: ')) #pedimos al usuario que ingrese el texto
#Imprimimos los resultados
print("Sentimiento: " + text["sentiment"])
print("Polaridad:" + str(text["polarity"]))
print("Subjetividad:" + str(text["subjectivity"]))
