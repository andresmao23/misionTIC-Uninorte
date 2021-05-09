if __name__=="__main__":
    foco_ecogenico = {'FE1':0, 'FE2':3, 'FE3':6, 'FE4':9}
    foco_eco = []
    puntaje = 0

    composicion = input("Digite el código de la composición: ").upper()
    ecogenicidad = input("Digite el código de la ecogenicidad: ").upper()
    forma = input("Digite el código de la forma: ").upper()
    margen = input("Digite el código de la margen: ").upper()

    i = 0
    while i < 4:
        fe = input(f"Digite el valor del Foco Ecogenico {i+1} (0 o 1): ")
        foco_eco.append(fe)
        i=i+1
    
    tamanio = float(input("Digite el valor del tamaño: "))

    if composicion == 'C1':
        puntaje = puntaje + 0
    elif composicion == 'C2':
        puntaje = puntaje + 0
    elif composicion == 'C3':
        puntaje = puntaje + 3
    elif composicion == 'C4':
        puntaje = puntaje + 6
    
    if ecogenicidad == 'E1':
        puntaje = puntaje + 0
    elif ecogenicidad == 'E2':
        puntaje = puntaje + 3
    elif ecogenicidad == 'E3':
        puntaje = puntaje + 6
    elif ecogenicidad == 'E4':
        puntaje = puntaje + 9
    
    if forma == 'F1':
        puntaje = puntaje + 0
    elif forma == 'F2':
        puntaje = puntaje + 9
    
    if margen == 'M1':
        puntaje = puntaje + 0
    elif margen == 'M2':
        puntaje = puntaje + 0
    elif margen == 'M3':
        puntaje = puntaje + 6
    elif margen == 'M4':
        puntaje = puntaje + 9
    
    if foco_eco[0] == '1':
        puntaje = puntaje + foco_ecogenico['FE1']
    if foco_eco[1] == '1':
        puntaje = puntaje + foco_ecogenico['FE2']
    if foco_eco[2] == '1':
        puntaje = puntaje + foco_ecogenico['FE3']
    if foco_eco[3] == '1':
        puntaje = puntaje + foco_ecogenico['FE4']

    print("Puntaje: ", puntaje)

    if puntaje >= 0 and puntaje <= 5:
        print("Sin riesgo, No AAF")
    if puntaje >= 6 and puntaje <= 8:
        print("Alerta azul, No AAF")
    if puntaje >= 9 and puntaje <= 11:
        if tamanio >= 2.5:
            print("Alerta verde, AAF")
        else:
            print("Alerta verde, Seguimiento")
    if puntaje >= 12 and puntaje <= 18:
        if tamanio >= 1.5:
            print("Alerta amarilla, AAF")
        else:
            print("Alerta amarilla, Seguimiento")
    if puntaje >= 19:
        if tamanio >= 1:
            print("Alerta roja, AAF")
        else:
            print("Alerta roja, Seguimiento")
