# Reto 1 - Seleccion de becas para minorias
import operator
# Variables
salario_minimo = 908526

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

lista_candidatos = []
candidato = {'re':'', 'es':'', 'inf':0, 'puntaje':0, 'pasa':False}

cant_errores = 0

while True:
    cantidad = int(input("Numero de personas a aplicar: "))
    if cantidad > 0:
        break
contador = 1
while True:
    datos_candidato = input("Digite los datos del candidato (etnia, estrato, ingreso familiar): ")
    datos_candidato = datos_candidato.split(",")
    #print(datos_candidato)
    re = datos_candidato[0].replace(" ", "_")
    es = datos_candidato[1]
    inf = float(datos_candidato[2])
    candidato['re'] = re
    candidato['es'] = es
    candidato['inf'] = inf
    lista_candidatos.append(candidato)
    candidato = {'re': '', 'es': '', 'inf': 0, 'puntaje': 0, 'pasa': -1}
    contador = contador + 1
    if contador > cantidad:
        break
print(10*'*', 'LISTA DE CANDIDATOS ANTES', 10*'*')
print(lista_candidatos)
print(10*'*', 'LISTA DE CANDIDATOS ANTES', 10*'*')
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

    if (candidato['inf'] < salario_minimo):
        candidato['inf'] = ingreso_nucleo_familiar['menos_un_salario']
    elif (candidato['inf'] >= salario_minimo and candidato['inf'] <= 2*salario_minimo):
        candidato['inf'] = ingreso_nucleo_familiar['uno_dos_salarios']
    elif (candidato['inf'] >= 2*salario_minimo and candidato['inf'] < 4*salario_minimo):
        candidato['inf'] = ingreso_nucleo_familiar['dos_cuatro_salarios']
    elif (candidato['inf'] >= 4*salario_minimo and candidato['inf'] < 5*salario_minimo):
        candidato['inf'] = ingreso_nucleo_familiar['cuatro_cinco_salarios']
    elif (candidato['inf'] >= 5*salario_minimo):
        candidato['inf'] = ingreso_nucleo_familiar['mas_cinco_salarios']
    # Si flag_re o flag_es son 0, es porque hubo un error en las estradas de reconocimiento etnico y/o estrato social
    # y se ponen en -1 para que no sean tenidos en cuenta
    if (flag_re== 0 or flag_es == 0):
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
print(10*'*', 'LISTA DE CANDIDATOS DESPUES', 10*'*')
print(lista_candidatos)
print(10*'*', 'LISTA DE CANDIDATOS DESPUES', 10*'*')

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
'''Obtengo una lista cuyos valores están repetidos en el diccionario anterior (salida_ordenada)
    Dicha lista queda ordenada en orden alfabetico pero ascendentemente'''
sorted_list = sorted(salida_ordenada, key=lambda k: (salida_ordenada[k], k))
# Ordeno la lista alfabeticamente, pero de manera descendente que es como la necesito finalmente (Segundo criterio de ordenamiento)
sorted_list_mao = sorted_list[::-1]

for elemento in sorted_list_mao:
    print(elemento, salida_ordenada[elemento])
