# Reto 1 - Seleccion de becas para minorias

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

while True:
    cantidad = int(input("Numero de personas a aplicar: "))
    if cantidad > 0:
        break
contador = 1
while True:
    re = input("Digite la etnia a la que pertenece: ")
    re = re.replace(" ", "_")  # reemplazar espacios por guion bajo
    es = input("Digite el estrato: ")
    inf = float(input("Digite el ingreso familiar: "))
    candidato['re'] = re
    candidato['es'] = es
    candidato['inf'] = inf
    lista_candidatos.append(candidato)
    candidato = {'re': '', 'es': '', 'inf': 0, 'puntaje': 0, 'pasa': False}
    contador = contador + 1
    if contador > cantidad:
        break
print(10*'*', 'LISTA DE CANDIDATOS ANTES', 10*'*')
print(lista_candidatos)
print(10*'*', 'LISTA DE CANDIDATOS ANTES', 10*'*')
for candidato in lista_candidatos:
    flag_re = 0 # bandera para controlar la variable re
    flag_es = 0 # bandera para controlar la variable es
    for key in reconocimiento_etnico:
        if (candidato['re'] == key):
            candidato['re'] = reconocimiento_etnico[key]
            flag_re = 1

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

    if (flag_re== 0 or flag_es == 0):
        candidato['re'] = -1
        candidato['es'] = 0

    puntaje_por_candidato = candidato['re'] + int(candidato['es']) + candidato['inf']
    candidato['puntaje'] = puntaje_por_candidato
    if (puntaje_por_candidato >= 25):
        candidato['pasa'] = True
print(10*'*', 'LISTA DE CANDIDATOS DESPUES', 10*'*')
print(lista_candidatos)
print(10*'*', 'LISTA DE CANDIDATOS DESPUES', 10*'*')

cant_candidatos_pasan = 0

cont_sin_reconocimiento = 0
cont_afrodescendiente = 0
cont_indigena = 0
cont_raizal = 0
cont_palenquero = 0
cont_gitano = 0

for candidato in lista_candidatos:
    if candidato['pasa'] == True:
        cant_candidatos_pasan = cant_candidatos_pasan + 1
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

print(cant_candidatos_pasan)
print('sin reconocimiento {}'.format(cont_sin_reconocimiento))
print('afrodescendiente {}'.format(cont_afrodescendiente))
print('indigena {}'.format(cont_indigena))
print('raizal {}'.format(cont_raizal))
print('palenquero {}'.format(cont_palenquero))
print('gitano {}'.format(cont_gitano))