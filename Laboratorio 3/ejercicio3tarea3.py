#luis Fernando Velasco Gracía
#Ejerciio 3
#para ejecutar este programa se debera poner en python numeros(numero 1,numero 2,numero 3,numero4)
def numeros(a,b,c):
  if a<b and b<c:
    print a, b, c
  elif a<c and c<b:
    print a, c, b
  elif b<a and a<c:
    print b, a, c
  elif b<c and c<a:
    print b, c, a
  elif c<a and a<b:
    print c, a, b
  elif c<b and b<a:
    print c, b, a
