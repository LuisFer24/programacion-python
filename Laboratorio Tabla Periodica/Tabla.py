#<>
#Luis Fernando Velasco García
#Tabla periodica
#Para ejecutar el programa lo primero es que se debe agregar algun dato del elemento,su simbolo o nombre (con sus mayusculas correspondientes)

import csv
a=raw_input("Introduce alguna caracteristica del elemento: ")
def TablaPe(x):
    x=a
    with open('ptable.csv') as csvarchivo:
        entrada = csv.reader(csvarchivo)
        mod=[]
        for reg in entrada:
            mod.append(reg)
        for i in range(118):
            if x in mod[i]:
                print mod[i]
salida=TablaPe(a)
