abc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
valores = [1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10]
tup = zip(abc,valores)
dic = dict(tup)
palabra = input('Ingrese una palabra: ')
suma = 0
for letra in palabra.upper():
    suma += dic[letra]
print('El valor de la palabra es: ', suma)