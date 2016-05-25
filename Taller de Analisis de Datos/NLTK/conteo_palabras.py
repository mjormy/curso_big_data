# Curso BigData & Data Analytics by Handytec
# Fecha: Marzo-2016
# Descripcion: Programa que cuenta las ocurrencias de palabras en un texto

import nltk
from nltk.corpus import cess_esp as cess
from nltk.corpus import PlaintextCorpusReader
from nltk.text import Text
from string import punctuation
from collections import Counter
from nltk.corpus import stopwords
import string
import sys
import codecs

#Usamos la libreria nltk para considerar los stopwords
default_stopwords = set(nltk.corpus.stopwords.words('spanish'))
#Leemos el archivo que queremos procesar
corpus = nltk.corpus.PlaintextCorpusReader('.', 'starwars.txt')

#Contamos e Imprimimos el nro. de oraciones
print "Oraciones =", len(corpus.sents())
#COntamos e Imprimimos el nro. de palabras
print "Palabras =", len([word for sentence in corpus.sents() for word in sentence])

#Comenzamos a contar la ocurrencia de palabras que constan en el archivo 
palabras=corpus.words()

#Unicamente consideramos palabras mayores a 4 letras y las tokenizamos
palabras = [word for word in palabras if len(word) > 4]

#Utilizamos la utilidad para obtener las palabras mas comunes
fdist = nltk.FreqDist(palabras)
print fdist

#Imprimimos el top 20 de ocurrencias en orden descendente
for word, frequency in fdist.most_common(20):
    print('%s--->%d' % (word, frequency)).encode('utf-8')