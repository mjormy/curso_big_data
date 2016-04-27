
listanegra = ['es', 'la', 'el', 'los', 'las', 'ellos']
listanegra += ['si', 'eso', 'no', 'que', 'lo', 'y']
listanegra += ['a', 'un', 'uno', 'unos', 'su', 'suyo']
listanegra += ['se', 'en', 'de', 'con', 'al', 'una']

#Funciion que lee el texto del archivo
def leerarchivo():
    archi=open('texto.txt','r')
    lineas=archi.read()
    archi.close()
    return lineas

#Funcion que Ignora las palabras que esten en la lista negra, retorna el listado con palabras deseadas
def removerListaNegra(listaPalabrasP, listanegraP):
    return [w for w in listaPalabrasP if w not in listanegraP]

#Funcion de ordenamiento
def ordenarFreqDict(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    aux.reverse()
    return aux

#Funcion para conteo
def listaPalabrasAFrecDict(listaPalabrasP):
    palabraFrec = [listaPalabrasP.count(p) for p in listaPalabrasP]
    return dict(zip(listaPalabrasP,palabraFrec))

#1. Leer archivo
texto = leerarchivo()
#2. Separar palabras y ponerlas en una lista
listaPalabras = texto.split()
#3. Ignorar palabras en la lista negra
listaPalabras = removerListaNegra(listaPalabras,listanegra)
#4. Convertir lista en diccionario
diccionario = listaPalabrasAFrecDict(listaPalabras)
#5. Ordenar diccionario
diccionarioOrdenado = ordenarFreqDict(diccionario)

#6. Presentar resultados
for s in diccionarioOrdenado: print str(s)

