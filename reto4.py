# Reto 4 - Seleccion de becas para minorias
import operator
# Variables
salario_minimo = 908526

dias = 7

reconocimiento_etnico = {}
reconocimiento_etnico['sin_reconocimiento'] = 0
reconocimiento_etnico['afrodescendiente'] = 4
reconocimiento_etnico['indigena'] = 5
reconocimiento_etnico['raizal'] = 6
reconocimiento_etnico['palenquero'] = 7
reconocimiento_etnico['gitano'] = 8

estrato_socioeconomico = {}
estrato_socioeconomico['1'] = 10
estrato_socioeconomico['2'] = 8
estrato_socioeconomico['3'] = 6
estrato_socioeconomico['4'] = 2
estrato_socioeconomico['5'] = 0
estrato_socioeconomico['6'] = 0

ingreso_nucleo_familiar = {}
ingreso_nucleo_familiar['menos_un_salario'] = 15
ingreso_nucleo_familiar['uno_dos_salarios'] = 9
ingreso_nucleo_familiar['dos_cuatro_salarios'] = 7
ingreso_nucleo_familiar['cuatro_cinco_salarios'] = 4
ingreso_nucleo_familiar['mas_cinco_salarios'] = 0

lista_candidatos_dia1 = []
lista_candidatos_dia2 = []
lista_candidatos_dia3 = []
lista_candidatos_dia4 = []
lista_candidatos_dia5 = []
lista_candidatos_dia6 = []
lista_candidatos_dia7 = []
#candidato = {'re':'', 'es':'', 'inf':0, 'puntaje':0, 'pasa':False}

cant_errores = 0

matriz_etnias = []
matriz_estratos = []
matriz_ingresos = []

while True:
    cantidad = int(input("Numero de personas a aplicar: "))
    if cantidad > 0:
        break
contador = 1
while True:
    matriz_aux = []
    for i in range(cantidad):
        datos = input("Digite los datos de la matriz {}: ".format(i))
        matriz_aux.append(datos.split(" "))
    if contador == 1:
        matriz_etnias = matriz_aux
    elif contador == 2:
        matriz_estratos = matriz_aux
    elif contador == 3:
        matriz_ingresos = matriz_aux
    contador = contador + 1
    if contador > 3:
        break
print(matriz_etnias)
print(matriz_estratos)
print(matriz_ingresos)

for dia in range(dias):
    for j in range(cantidad+1):
        candidato = {'re': '', 'es': '', 'inf': 0, 'puntaje': 0, 'pasa': False}
        candidato['re'] = matriz_etnias[j][dia]
        candidato['es'] = matriz_estratos[j][dia]
        candidato['inf'] = matriz_ingresos[j][dia]
        if dia == 0:
            lista_candidatos_dia1.append(candidato)
        elif dia == 1:
            lista_candidatos_dia2.append(candidato)
        elif dia == 2:
            lista_candidatos_dia3.append(candidato)
        elif dia == 3:
            lista_candidatos_dia4.append(candidato)
        elif dia == 4:
            lista_candidatos_dia5.append(candidato)
        elif dia == 5:
            lista_candidatos_dia6.append(candidato)
        elif dia == 6:
            lista_candidatos_dia7.append(candidato)
print(10*'*', 'LISTA DECANDIDATOS DEL DÍA 1', 10*'*')
print(lista_candidatos_dia1)
print(10*'*', 'LISTA DE CANDIDATOS DEL DIA 2', 10*'*')
print(lista_candidatos_dia2)
print(10*'*', 'LISTA DE CANDIDATOS DEL DIA 3', 10*'*')
print(lista_candidatos_dia3)
print(10*'*', 'LISTA DE CANDIDATOS DEL DIA 4', 10*'*')
print(lista_candidatos_dia4)
print(10*'*', 'LISTA DE CANDIDATOS DEL DIA 5', 10*'*')
print(lista_candidatos_dia5)
print(10*'*', 'LISTA DE CANDIDATOS DEL DIA 6', 10*'*')
print(lista_candidatos_dia6)
print(10*'*', 'LISTA DE CANDIDATOS DEL DIA 7', 10*'*')
print(lista_candidatos_dia7)

'''
def evaluar_lista_candidatos(lista_candidatos):    
    for candidato in lista_candidatos:
        flag_re = 0 # bandera para controlar la variable re
        flag_es = 0 # bandera para controlar la variable es
        # Cuando flag_re = 1, es porque todo anda bien
        for key in reconocimiento_etnico:
            if (candidato['re'] == key):
                candidato['re'] = reconocimiento_etnico[key]
                flag_re = 1
        # Cuando flag_es = 1, es porque todo anda bien
        for key in estrato_socioeconomico:
            if (candidato['es'] == key):
                candidato['es'] = estrato_socioeconomico[key]
                flag_es = 1

        if (float(candidato['inf']) < salario_minimo):
            candidato['inf'] = ingreso_nucleo_familiar['menos_un_salario']
        elif (float(candidato['inf']) >= salario_minimo and float(candidato['inf']) <= 2*salario_minimo):
            candidato['inf'] = ingreso_nucleo_familiar['uno_dos_salarios']
        elif (float(candidato['inf']) >= 2*salario_minimo and float(candidato['inf']) < 4*salario_minimo):
            candidato['inf'] = ingreso_nucleo_familiar['dos_cuatro_salarios']
        elif (float(candidato['inf']) >= 4*salario_minimo and float(candidato['inf']) < 5*salario_minimo):
            candidato['inf'] = ingreso_nucleo_familiar['cuatro_cinco_salarios']
        elif (float(candidato['inf']) >= 5*salario_minimo):
            candidato['inf'] = ingreso_nucleo_familiar['mas_cinco_salarios']
        # Si flag_re o flag_es son 0, es porque hubo un error en las estradas de reconocimiento etnico y/o estrato social
        # y se ponen en -1 para que no sean tenidos en cuenta
        if (flag_re == 0 or flag_es == 0):
            candidato['re'] = -1
            candidato['es'] = -1

        if candidato['re'] == -1 or candidato['es'] == -1:
            candidato['puntaje'] = -1
        if candidato['puntaje'] != -1:
            puntaje_por_candidato = candidato['re'] + int(candidato['es']) + candidato['inf']
            candidato['puntaje'] = puntaje_por_candidato
            if (puntaje_por_candidato >= 25):
                candidato['pasa'] = True
            else:
                candidato['pasa'] = False

    cant_candidatos_pasan = 0
    cant_candidatos_no_pasan = 0

    cont_sin_reconocimiento = 0
    cont_afrodescendiente = 0
    cont_indigena = 0
    cont_raizal = 0
    cont_palenquero = 0
    cont_gitano = 0

    # Se suman los candidatos que continuan, los que no continuan y la cantidad de entradas erroneas
    for candidato in lista_candidatos:
        if candidato['pasa'] == True:
            cant_candidatos_pasan = cant_candidatos_pasan + 1
        elif candidato['pasa'] == False:
            cant_candidatos_no_pasan = cant_candidatos_no_pasan + 1
        elif candidato['pasa'] == -1:
            cant_errores = cant_errores + 1

        if candidato['re'] == reconocimiento_etnico['sin_reconocimiento']:
            cont_sin_reconocimiento = cont_sin_reconocimiento + 1
        elif candidato['re'] == reconocimiento_etnico['afrodescendiente']:
            cont_afrodescendiente = cont_afrodescendiente + 1
        elif candidato['re'] == reconocimiento_etnico['indigena']:
            cont_indigena = cont_indigena + 1
        elif candidato['re'] == reconocimiento_etnico['raizal']:
            cont_raizal = cont_raizal + 1
        elif candidato['re'] == reconocimiento_etnico['palenquero']:
            cont_palenquero = cont_palenquero + 1
        elif candidato['re'] == reconocimiento_etnico['gitano']:
            cont_gitano = cont_gitano + 1

    salida = {
        'sin reconocimiento':cont_sin_reconocimiento,
        'afrodescendiente':cont_afrodescendiente,
        'indigena': cont_indigena,
        'raizal':cont_raizal,
        'palenquero':cont_palenquero,
        'gitano':cont_gitano
    }
    print(cant_candidatos_pasan, ' ', cant_candidatos_no_pasan, ' ', cant_errores)
    # Ordenar el diccionario de acuerdo a su valor (Primer criterio de ordenamiento)
    salida_ordenada = dict(sorted(salida.items(), key=operator.itemgetter(1),reverse=True))

    sorted_list = sorted(salida_ordenada, key=lambda k: (salida_ordenada[k], k))
    # Ordeno la lista alfabeticamente, pero de manera descendente que es como la necesito finalmente (Segundo criterio de ordenamiento)
    sorted_list_mao = sorted_list[::-1]

    for elemento in sorted_list_mao:
        print(elemento, salida_ordenada[elemento])
    return lista_candidatos, cant_candidatos_pasan

cant_candidatos_pasan_dia1 = 0
cant_candidatos_pasan_dia2 = 0
cant_candidatos_pasan_dia3 = 0
cant_candidatos_pasan_dia4 = 0
cant_candidatos_pasan_dia5 = 0
cant_candidatos_pasan_dia6 = 0
cant_candidatos_pasan_dia7 = 0

lista_candidatos_dia1, cant_candidatos_pasan_dia1 = evaluar_lista_candidatos(lista_candidatos_dia1)
lista_candidatos_dia2, cant_candidatos_pasan_dia2 = evaluar_lista_candidatos(lista_candidatos_dia2)
lista_candidatos_dia3, cant_candidatos_pasan_dia3 = evaluar_lista_candidatos(lista_candidatos_dia3)
lista_candidatos_dia4, cant_candidatos_pasan_dia4 = evaluar_lista_candidatos(lista_candidatos_dia4)
lista_candidatos_dia5, cant_candidatos_pasan_dia5 = evaluar_lista_candidatos(lista_candidatos_dia5)
lista_candidatos_dia6, cant_candidatos_pasan_dia6 = evaluar_lista_candidatos(lista_candidatos_dia6)
lista_candidatos_dia7, cant_candidatos_pasan_dia7 = evaluar_lista_candidatos(lista_candidatos_dia7)

print(10*'*', 'LISTA DECANDIDATOS DEL DÍA 1 NUEVA', 10*'*')
print(lista_candidatos_dia1)
print(10*'*', 'LISTA DE CANDIDATOS DEL DIA 2 NUEVA', 10*'*')
print(lista_candidatos_dia2)
print(10*'*', 'LISTA DE CANDIDATOS DEL DIA 3 NUEVA', 10*'*')
print(lista_candidatos_dia3)
print(10*'*', 'LISTA DE CANDIDATOS DEL DIA 4 NUEVA', 10*'*')
print(lista_candidatos_dia4)
print(10*'*', 'LISTA DE CANDIDATOS DEL DIA 5 NUEVA', 10*'*')
print(lista_candidatos_dia5)
print(10*'*', 'LISTA DE CANDIDATOS DEL DIA 6 NUEVA', 10*'*')
print(lista_candidatos_dia6)
print(10*'*', 'LISTA DE CANDIDATOS DEL DIA 7 NUEVA', 10*'*')
print(lista_candidatos_dia7)'''