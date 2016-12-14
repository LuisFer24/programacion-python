#Luis Fernando Velasco García
#Ejercicio 1

import math as m
def distancia(x1,y1,x2,y2):
    x1=m.radians(x1)
    y1=m.radians(y1)
    x2=m.radians(x2)
    y2=m.radians(y2)

    distancia=6371.01*m.acos(m.sin(x1)*m.sin(x2)+m.cos(x1)*m.cos(x2)*m.cos(y1-y2))
    return distancia

print distancia
