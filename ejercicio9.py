import string
frase = input('Ingrese una palabra o frase: ')
lis = []
no_es = False
for caracter in frase:
    if caracter not in string.punctuation + ' ':
        if caracter in lis:
            no_es = True
        else:
            lis.append(caracter)
if(not no_es):
    print('La palabra o frase ingresada es un Heterograma')        