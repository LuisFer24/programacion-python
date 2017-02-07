#<>
#Luis Fernando Velasco García
#Ejercicio 1
#para ejecutar el programa se debe abrir python en la carpeta donde se encuentra el texto.txt, y ejecutar el programa
a=raw_input("Introduce el nombre de un archivo.txt(debe estar en la carpeta actual): ")
b=input("Introduzca el nùmero de lineas que desea leer: ")
def lector(x,y):
    x=a
    y=b
    archivo=open(x,"r")
    for i in range(b):
        print archivo.readline()

output=lector(a,b)
