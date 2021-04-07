import string
def nombres_en_ambas(lista1, lista2):
    """Función que recibe dos listas con nombres e imprime los nombres 
    coincidentes en ambas (es case sensitive)"""
    lista_concidencias = [nom1 for nom1 in lista1 if nom1.upper() in lista2]
    print('Los nombres que se encuentran en ambas listas son: \n')
    print(sorted(list(set(lista_concidencias))))
nombres1="""'Agustin',
 'Alan',
 'Andrés',
 'Ariadna',
 'Bautista',
 'CAROLINA',
 'CESAR',
 'David',
 'Diego',
 'Dolores',
 'DYLAN',
 'ELIANA',
 'Emanuel',
 'Fabián',
 'Facundo',
 'Facundo',
 'FEDERICO',
 'FEDERICO',
 'GONZALO',
 'Gregorio',
 'Ignacio',
 'Jonathan',
 'Jonathan',
 'Jorge',
 'JOSE',
 'JUAN',
 'Juan',
 'Juan',
 'Julian',
 'Julieta',
 'LAUTARO',
 'Leonel',
 'LUIS',
 'Luis',
 'Marcos',
 'María',
 'MATEO',
 'Matias',
 'Nicolás',
 'NICOLÁS',
 'Noelia',
 'Pablo',
 'Priscila',
 'TOMAS',
 'Tomás',
 'Ulises',
 'Yanina'"""
nombres2="""'Agustin',
 'AGUSTIN',
 'Agustín',
 'Ailen',
 'Alfredo',
 'Amalia',
 'Ariana',
 'Bautista',
 'Braian',
 'Carla',
 'CESAR',
 'Daniel',
 'Diego',
 'ELIANA',
 'Facundo',
 'Facundo',
 'Facundo',
 'Facundo',
 'Federico',
 'Federico',
 'Flavia',
 'Francisco',
 'Germán',
 'Guido',
 'GUSTAVO',
 'Hilario',
 'Ignacio',
 'IVAN',
 'Jimmy',
 'Joaquín',
 'Jose',
 'Josue',
 'JUAN',
 'Juan',
 'Laura',
 'LAURA',
 'Lautaro',
 'Lautaro',
 'Ludmila',
 'Marcos',
 'Marcos',
 'MARIANELA',
 'MARTIN',
 'MATEO',
 'Mateo',
 'Matias',
 'MAURO',
 'Maximiliano',
 'NESTOR',
 'Nicolas',
 'Pedro',
 'Ramiro',
 'Sofía',
 'Tobias',
 'Tomás',
 'Tomás',
 'Ulises',
 'Yanina'"""
eval1 = """81,
 60,
 72,
 24,
 15,
 91,
 12,
 70,
 29,
 42,
 16,
 3,
 35,
 67,
 10,
 57,
 11,
 69,
 12,
 77,
 13,
 86,
 48,
 65,
 51,
 41,
 87,
 43,
 10,
 87,
 91,
 15,
 44,
 85,
 73,
 37,
 42,
 95,
 18,
 7,
 74,
 60,
 9,
 65,
 93,
 63,
 74""" 
eval2 = """30,
 95,
 28,
 84,
 84,
 43,
 66,
 51,
 4,
 11,
 58,
 10,
 13,
 34,
 96,
 71,
 86,
 37,
 64,
 13,
 8,
 87,
 14,
 14,
 49,
 27,
 55,
 69,
 77,
 59,
 57,
 40,
 96,
 24,
 30,
 73,
 95,
 19,
 47,
 15,
 31,
 39,
 15,
 74,
 33,
 57,
 10"""
#Creación de listas correspondientes para los datos dados
eval_1 = [int(ev.strip(string.punctuation)) for ev in eval1.split()]
eval_2 = [int(ev.strip(string.punctuation)) for ev in eval2.split()]
lista_1 = [nom.strip(string.punctuation) for nom in nombres1.split()]
lista_2 = [nom.strip(string.punctuation).upper() for nom in nombres2.split()]
#Primer inciso, se indican que nombres se encuentran en ambas listas
nombres_en_ambas(lista_1,lista_2)
#Segundo inciso, todavía no entendí bien el enunciado, falta arreglar
suma_notas = [sum(i) for i in list(zip(eval_1,eval_2))]
#lista_total = list(zip(lista_1,suma_notas))
print('{:>3}{:<14}{:^8}{:^8}{:^8}'.format('','Nombre','Eval1','Eval2','Total'))
for i in range(len(suma_notas)):
    print('{:>3}{:<14}{:^8}{:^8}{:^8}'.format(str(i) + ' ',lista_total[i][0],eval_1[i],eval_2[i],suma_notas[i]))
