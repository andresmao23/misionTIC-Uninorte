# Reto 1 - Seleccion de becas para minorias

# Variables
salario_minimo = 908526
puntaje = 0
flag_re = 0 # bandera para controlar la variable re
flag_es = 0 # bandera para controlar la variable es
flag_inf = 0 # bandera para controlar la variable inf

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
ingreso_nucleo_familiar['un_salario'] = 9
ingreso_nucleo_familiar['dos_tres_salarios'] = 7
ingreso_nucleo_familiar['cuatro_salarios'] = 4
ingreso_nucleo_familiar['cinco_salarios'] = 0

salidas = {}
salidas['error'] = 'Se presento un error'
salidas['ok'] = 'El candidato continua en el proceso de seleccion'
salidas['no_pasa'] = 'El candidato NO continua en el proceso de seleccion'

re = input("Digite la etnia a la que pertenece: ")
es = input("Digite el estrato: ")
inf = float(input("Digite el ingreso familiar: "))

re = re.replace(" ", "_") # reemplazar espacios por guion bajo

for key in reconocimiento_etnico:
    if (re == key):
        re = reconocimiento_etnico[key]
        flag_re = 1

for key in estrato_socioeconomico:
    if (es == key):
        es = estrato_socioeconomico[key]
        flag_es = 1

if (inf < salario_minimo):
    inf = ingreso_nucleo_familiar['menos_un_salario']
elif (inf == salario_minimo):
    inf = ingreso_nucleo_familiar['un_salario']
elif (inf > salario_minimo and inf <= 3*salario_minimo):
    inf = ingreso_nucleo_familiar['dos_tres_salarios']
elif (inf == 4*salario_minimo):
    inf = ingreso_nucleo_familiar['cuatro_salarios']
elif (inf == 5*salario_minimo):
    inf = ingreso_nucleo_familiar['cinco_salarios']
else:
    flag_inf = 1

if (flag_inf == 1 or flag_re == 0 or flag_es == 0):
    print(salidas['error'])
    quit()

puntaje = re + es + inf
if (puntaje < 25 and flag_inf == 0):
    print(salidas['no_pasa'])
elif (puntaje >= 25 and flag_inf == 0):
    print(salidas['ok'])
