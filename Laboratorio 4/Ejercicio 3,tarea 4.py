#<>
#Luis Fernando Velasco García
#Ejercicio 3
#para ejecutar el programa se debe abrir python en la carpeta donde se encuentran los archivos tipo txt, y ejecutar el programa
x=raw_input("Introduzca el nombre de un archivo:")
y=raw_input("Introduzca el nombre del archivo una vez editado:")
def editor(a,b):
    a=x
    b=y
    texto=open(a,'r')
    edicion=0
    texto2=open(b,'w')
    copy=texto.readlines()
    for i in copy:
        edicion=edicion+1
        texto2.write(str(edicion)+str(i)+" ")
        print edicion
        print i
output=editor(x,y)
