import operator
matriz = []

def quitar_contador_cero(d):
    keys = [k for k, v in d.items() if v == 0]
    for x in keys:
        del d[x]
    return d

with open('data.csv','rt',encoding='utf8') as f:
    f.readline()
    for linea in f:
        datos = linea.replace('\n','').split(',')
        matriz.append(datos)
    ciudad = input()
    contador_candidatos_por_ciudad = 0
    cont_sin_reconocimiento = 0
    cont_afrodescendiente = 0
    cont_indigena = 0
    cont_raizal = 0
    cont_palenquero = 0
    cont_gitano = 0
    lista_ingresos = []
    for candidato in matriz:
        if ciudad==candidato[2] and candidato[-1]=='1':
            contador_candidatos_por_ciudad += 1
            lista_ingresos.append(int(candidato[6]))
            if candidato[4] == 'sin_reconocimiento':
                cont_sin_reconocimiento = cont_sin_reconocimiento + 1
            elif candidato[4] == 'afrodescendiente':
                cont_afrodescendiente = cont_afrodescendiente + 1
            elif candidato[4] == 'indigena':
                cont_indigena = cont_indigena + 1
            elif candidato[4] == 'raizal':
                cont_raizal = cont_raizal + 1
            elif candidato[4] == 'palenquero':
                cont_palenquero = cont_palenquero + 1
            elif candidato[4] == 'gitano':
                cont_gitano = cont_gitano + 1

        salida = {
            'sin reconocimiento':cont_sin_reconocimiento,
            'afrodescendiente':cont_afrodescendiente,
            'indigena': cont_indigena,
            'raizal':cont_raizal,
            'palenquero':cont_palenquero,
            'gitano':cont_gitano
        }
        salida1 = quitar_contador_cero(salida)
        lista_salida = []
        for k,v in salida1.items():
            lista_salida.append((k,v))
    #print(lista_salida)
    ingreso_minimo = min(lista_ingresos)
    ingreso_maximo = max(lista_ingresos)
    ingreso_promedio = sum(lista_ingresos)/contador_candidatos_por_ciudad
    print(contador_candidatos_por_ciudad)
    print('{} {} {:.2f}'.format(ingreso_minimo, ingreso_maximo, ingreso_promedio))
    lista_salida_ordenada = sorted(lista_salida, key=lambda row:(row[0]))
    lista_salida_ordenada = sorted(lista_salida_ordenada, key=lambda row:(row[1]), reverse=True)
    for i in lista_salida_ordenada:
        print(*i)