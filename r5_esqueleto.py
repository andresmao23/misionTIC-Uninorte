# Cargar los datos del archivo a una estructura en memoria
# a) Averiguar la estructura del archivo
#    Headers (Títulos) : Yes   ==> Ignore
#    Footres (Summary) : no
#    Field Separator   : comma(,) 
#    Record Separator  : Newline (\n)
# a) Abrir el archivo para lectura
matriz = []
with open('data.csv','rt',encoding='utf8') as f:
    # Headers ==> Ignore
    f.readline()
    # Procesar las demás lineas
    for linea in f:
        # Separar (split)
        datos = linea.replace('\n','').split(',')
        # Transformar
        datos[0]=datos[0].upper()
        datos[1]=int(datos[1])
        datos[2]=int(datos[2])
        datos[3]=int(datos[3])
        datos[4]=float(datos[4])
        datos[5]=float(datos[5])
        datos[6]=datos[6].lower()
        # añadir al arreglo
        matriz.append(datos)
print(matriz)
