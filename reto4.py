# Reto 4 - Seleccion de becas para minorias
import operator
# Variables
salario_minimo = 908526

dias = 7

reconocimiento_etnico = {}
reconocimiento_etnico['1'] = 0 #sin_reconocimiento
reconocimiento_etnico['2'] = 4 #afrodescendiente
reconocimiento_etnico['3'] = 5 #indigena
reconocimiento_etnico['4'] = 6 #raizal
reconocimiento_etnico['5'] = 7 #palenquero
reconocimiento_etnico['6'] = 8 #gitano

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
#print(matriz_etnias)
#print(matriz_estratos)
#print(matriz_ingresos)

for i in range(len(matriz_etnias[0])):    
    for j in range(len(matriz_etnias)):
        '''print(matriz_etnias[j][i])
        print(matriz_estratos[j][i])
        print(matriz_ingresos[j][i])'''
        candidato = {'re': '', 'es': '', 'inf': 0, 'puntaje': 0, 'pasa': False}
        candidato['re'] = matriz_etnias[j][i]
        candidato['es'] = matriz_estratos[j][i]
        candidato['inf'] = matriz_ingresos[j][i]
        if i == 0:
            lista_candidatos_dia1.append(candidato)
        elif i == 1:
            lista_candidatos_dia2.append(candidato)
        elif i == 2:
            lista_candidatos_dia3.append(candidato)
        elif i == 3:
            lista_candidatos_dia4.append(candidato)
        elif i == 4:
            lista_candidatos_dia5.append(candidato)
        elif i == 5:
            lista_candidatos_dia6.append(candidato)
        elif i == 6:
            lista_candidatos_dia7.append(candidato)
'''print(10*'*', 'LISTA DECANDIDATOS DEL DÍA 1', 10*'*')
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
print(lista_candidatos_dia7)'''

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
    cant_errores = 0

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

        if candidato['re'] == reconocimiento_etnico['1']:
            cont_sin_reconocimiento = cont_sin_reconocimiento + 1
        elif candidato['re'] == reconocimiento_etnico['2']:
            cont_afrodescendiente = cont_afrodescendiente + 1
        elif candidato['re'] == reconocimiento_etnico['3']:
            cont_indigena = cont_indigena + 1
        elif candidato['re'] == reconocimiento_etnico['4']:
            cont_raizal = cont_raizal + 1
        elif candidato['re'] == reconocimiento_etnico['5']:
            cont_palenquero = cont_palenquero + 1
        elif candidato['re'] == reconocimiento_etnico['6']:
            cont_gitano = cont_gitano + 1

    salida = {
        'sin reconocimiento':cont_sin_reconocimiento,
        'afrodescendiente':cont_afrodescendiente,
        'indigena': cont_indigena,
        'raizal':cont_raizal,
        'palenquero':cont_palenquero,
        'gitano':cont_gitano
    }
    #print(cant_candidatos_pasan, ' ', cant_candidatos_no_pasan, ' ', cant_errores)
    # Ordenar el diccionario de acuerdo a su valor (Primer criterio de ordenamiento)
    salida_ordenada = dict(sorted(salida.items(), key=operator.itemgetter(1),reverse=True))

    #sorted_list = sorted(salida_ordenada, key=lambda k: (salida_ordenada[k], k))
    # Ordeno la lista alfabeticamente, pero de manera descendente que es como la necesito finalmente (Segundo criterio de ordenamiento)
    #sorted_list_mao = sorted_list[::-1]

    #for elemento in sorted_list_mao:
        #print(elemento, salida_ordenada[elemento])
    return lista_candidatos, cant_candidatos_pasan, salida_ordenada

cant_candidatos_pasan_dia1 = 0
cant_candidatos_pasan_dia2 = 0
cant_candidatos_pasan_dia3 = 0
cant_candidatos_pasan_dia4 = 0
cant_candidatos_pasan_dia5 = 0
cant_candidatos_pasan_dia6 = 0
cant_candidatos_pasan_dia7 = 0

salida_ordenada_dia1 = {}
salida_ordenada_dia2 = {}
salida_ordenada_dia3 = {}
salida_ordenada_dia4 = {}
salida_ordenada_dia5 = {}
salida_ordenada_dia6 = {}
salida_ordenada_dia7 = {}

lista_candidatos_dia1, cant_candidatos_pasan_dia1, salida_ordenada_dia1 = evaluar_lista_candidatos(lista_candidatos_dia1)
lista_candidatos_dia2, cant_candidatos_pasan_dia2, salida_ordenada_dia2 = evaluar_lista_candidatos(lista_candidatos_dia2)
lista_candidatos_dia3, cant_candidatos_pasan_dia3, salida_ordenada_dia3 = evaluar_lista_candidatos(lista_candidatos_dia3)
lista_candidatos_dia4, cant_candidatos_pasan_dia4, salida_ordenada_dia4 = evaluar_lista_candidatos(lista_candidatos_dia4)
lista_candidatos_dia5, cant_candidatos_pasan_dia5, salida_ordenada_dia5 = evaluar_lista_candidatos(lista_candidatos_dia5)
lista_candidatos_dia6, cant_candidatos_pasan_dia6, salida_ordenada_dia6 = evaluar_lista_candidatos(lista_candidatos_dia6)
lista_candidatos_dia7, cant_candidatos_pasan_dia7, salida_ordenada_dia7 = evaluar_lista_candidatos(lista_candidatos_dia7)

'''print(10*'*', 'LISTA DECANDIDATOS DEL DÍA 1 NUEVA', 10*'*')
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
print(lista_candidatos_dia7)
print(50*'*')
print(salida_ordenada_dia1)
print(salida_ordenada_dia2)
print(salida_ordenada_dia3)
print(salida_ordenada_dia4)
print(salida_ordenada_dia5)
print(salida_ordenada_dia6)
print(salida_ordenada_dia7)
print(50*'*')

def minimums(some_dict):
    positions = [] # output variable
    min_value = float("inf")
    for k, v in some_dict.items():
        if v == min_value:
            positions.append(k)
        if v < min_value:
            min_value = v
            positions = [] # output variable
            positions.append(k)

    return positions

key_min1 = min(salida_ordenada_dia1, key = lambda key: salida_ordenada_dia1[key])
key_min2 = min(salida_ordenada_dia2, key = lambda key: salida_ordenada_dia2[key])
key_min3 = min(salida_ordenada_dia3, key = lambda key: salida_ordenada_dia3[key])
key_min4 = min(salida_ordenada_dia4, key = lambda key: salida_ordenada_dia4[key])
key_min5 = min(salida_ordenada_dia5, key = lambda key: salida_ordenada_dia5[key])
key_min6 = min(salida_ordenada_dia6, key = lambda key: salida_ordenada_dia6[key])
key_min7 = min(salida_ordenada_dia7, key = lambda key: salida_ordenada_dia7[key])
print('{},{},{},{},{},{},{}'.format(key_min1, key_min2, key_min3, key_min4, key_min5, key_min6, key_min7))

key_max1 = max(salida_ordenada_dia1, key = lambda key: salida_ordenada_dia1[key])
key_max2 = max(salida_ordenada_dia2, key = lambda key: salida_ordenada_dia2[key])
key_max3 = max(salida_ordenada_dia3, key = lambda key: salida_ordenada_dia3[key])
key_max4 = max(salida_ordenada_dia4, key = lambda key: salida_ordenada_dia4[key])
key_max5 = max(salida_ordenada_dia5, key = lambda key: salida_ordenada_dia5[key])
key_max6 = max(salida_ordenada_dia6, key = lambda key: salida_ordenada_dia6[key])
key_max7 = max(salida_ordenada_dia7, key = lambda key: salida_ordenada_dia7[key])
print('{},{},{},{},{},{},{}'.format(key_max1, key_max2, key_max3, key_max4, key_max5, key_max6, key_max7))

DATA1=sorted(DATA,key=lambda row: (row[1],row[0]), reverse=True )
cont_sinreco = 0
cont_afro = 0
cont_ind = 0
cont_raiz = 0
cont_palenq = 0
cont_gita = 0
for k,v in salida_ordenada_dia1.items():
    if k == 'sin reconocimiento' and v == 1:
        cont_sinreco += 1
    if k == 'afrodescendiente' and v == 1:
        cont_afro += 1
    if k == 'indigena' and v == 1:
        cont_ind += 1
    if k == 'raizal' and v == 1:
        cont_raiz += 1
    if k == 'palenquero' and v == 1:
        cont_palenq += 1
    if k == 'gitano' and v == 1:
        cont_gita += 1
lista_contadores = []
lista_contadores.append(cont_sinreco)
lista_contadores.append(cont_afro)
lista_contadores.append(cont_ind)
lista_contadores.append(cont_raiz)
lista_contadores.append(cont_palenq)
lista_contadores.append(cont_gita)
l = lista_contadores.sort()
print(l)'''

valores = {'sin reconocimiento':1, 'afrodescendiente':2, 'indigena':3, 'raizal':4, 'palenquero':5, 'gitano':6}

def menor_por_dia(d1):
    keys = [k for k, v in d1.items() if v == 0]
    for x in keys:
        del d1[x]
    minval = min(d1.values())
    res = [k for k, v in d1.items() if v==minval]
    menor = valores[res[0]]
    clave = ''
    for x in res:
        if valores[x] <= menor:
            clave = x
    return clave

cont_s_mayor = 0
cont_a_mayor = 0
cont_i_mayor = 0
cont_r_mayor = 0
cont_p_mayor = 0
cont_g_mayor = 0

def mayor_por_dia(d):
    global cont_s_mayor
    global cont_a_mayor
    global cont_i_mayor
    global cont_r_mayor
    global cont_p_mayor
    global cont_g_mayor
    mayval = max(d.values())
    res = [k for k, v in d.items() if v==mayval]
    for i in res:
        if i == 'sin reconocimiento':
            cont_s_mayor += 1
        elif i == 'afrodescendiente':
            cont_a_mayor += 1
        elif i == 'indigena':
            cont_i_mayor += 1
        elif i == 'raizal':
            cont_r_mayor += 1
        elif i == 'palenquero':
            cont_p_mayor += 1
        elif i == 'gitano':
            cont_g_mayor += 1
    mayor = valores[res[0]]
    clave = ''
    for x in res:
        if valores[x] <= mayor:
            clave = x
    return clave

cont_s = 0
cont_a = 0
cont_i = 0
cont_r = 0
cont_p = 0
cont_g = 0

def menor_por_dia_incluyendo_cero(d):
    #keys = [k for k, v in d.items() if v == 0]
    global cont_s
    global cont_a
    global cont_i
    global cont_r
    global cont_p
    global cont_g
    minval = min(d.values())
    res = [k for k, v in d.items() if v==minval]
    for i in res:
        if i == 'sin reconocimiento':
            cont_s += 1
        elif i == 'afrodescendiente':
            cont_a += 1
        elif i == 'indigena':
            cont_i += 1
        elif i == 'raizal':
            cont_r += 1
        elif i == 'palenquero':
            cont_p += 1
        elif i == 'gitano':
            cont_g += 1
    menor = valores[res[0]]
    clave = ''
    for x in res:
        if valores[x] <= menor:
            clave = x
    return clave

s_o_d1 = dict(salida_ordenada_dia1)
s_o_d2 = dict(salida_ordenada_dia2)
s_o_d3 = dict(salida_ordenada_dia3)
s_o_d4 = dict(salida_ordenada_dia4)
s_o_d5 = dict(salida_ordenada_dia5)
s_o_d6 = dict(salida_ordenada_dia6)
s_o_d7 = dict(salida_ordenada_dia7)

print('{},{},{},{},{},{},{}\n'.format(menor_por_dia(s_o_d1),
                                    menor_por_dia(s_o_d2), 
                                    menor_por_dia(s_o_d3),
                                    menor_por_dia(s_o_d4),
                                    menor_por_dia(s_o_d5),
                                    menor_por_dia(s_o_d6),
                                    menor_por_dia(s_o_d7)))
menor_por_dia_incluyendo_cero(salida_ordenada_dia1)
menor_por_dia_incluyendo_cero(salida_ordenada_dia2)
menor_por_dia_incluyendo_cero(salida_ordenada_dia3)
menor_por_dia_incluyendo_cero(salida_ordenada_dia4)
menor_por_dia_incluyendo_cero(salida_ordenada_dia5)
menor_por_dia_incluyendo_cero(salida_ordenada_dia6)
menor_por_dia_incluyendo_cero(salida_ordenada_dia7)                                    
dict_menores = {
    'sin reconocimiento':cont_s,
    'afrodescendiente':cont_a,
    'indigena':cont_i,
    'raizal':cont_r,
    'palenquero':cont_p,
    'gitano':cont_g
}
print(cont_s, cont_a, cont_i, cont_r, cont_p, cont_g)
max_key = max(dict_menores.items(), key=operator.itemgetter(1))[0]
print(max_key)
print()                                    

print('{},{},{},{},{},{},{}\n'.format(mayor_por_dia(salida_ordenada_dia1),
                                    mayor_por_dia(salida_ordenada_dia2), 
                                    mayor_por_dia(salida_ordenada_dia3),
                                    mayor_por_dia(salida_ordenada_dia4),
                                    mayor_por_dia(salida_ordenada_dia5),
                                    mayor_por_dia(salida_ordenada_dia6),
                                    mayor_por_dia(salida_ordenada_dia7)))
dict_mayores = {
    'sin reconocimiento':cont_s_mayor,
    'afrodescendiente':cont_a_mayor,
    'indigena':cont_i_mayor,
    'raizal':cont_r_mayor,
    'palenquero':cont_p_mayor,
    'gitano':cont_g_mayor
}                                                                
print(cont_s_mayor, cont_a_mayor, cont_i_mayor, cont_r_mayor, cont_p_mayor, cont_g_mayor)
max_key_mayor = max(dict_mayores.items(), key=operator.itemgetter(1))[0]                                        
print(max_key_mayor)
print()
print("{} {} {} {} {} {} {}".format(cant_candidatos_pasan_dia1, cant_candidatos_pasan_dia2,
                                    cant_candidatos_pasan_dia3, cant_candidatos_pasan_dia4,
                                    cant_candidatos_pasan_dia5, cant_candidatos_pasan_dia6,
                                    cant_candidatos_pasan_dia7))