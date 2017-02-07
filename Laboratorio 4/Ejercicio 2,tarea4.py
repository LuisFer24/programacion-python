#<>
#Luis Fernando Velasco García
#Ejercicio 2
#para ejecutar el programa se debe abrir python en la carpeta donde se encuentran los archivos tipo txt, y ejecutar el programa
a=raw_input("Introduzca una lista de archivos(deben estar en la carpeta actual):").strip().split(',')
b=int(raw_input("Introduce las lineas que deseas unir: ").strip())
def lector2(x,y):
    x=a
    y=b
    for e in x:
        archivo=open((e),"r")
        for i in range(b):
            print archivo.readline()
output=lector2(a,b)
