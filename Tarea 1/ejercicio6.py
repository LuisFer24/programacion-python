#seis
def imc(e,p):
    imc=p/pow(e,2)
    print imc
    if imc<16:
        print "Delgadez severa"
    elif 16<imc<16.99:
        print "Delgadez moderada"
    elif 17<imc<18.49:
        print "Delgadez leve"
    elif 18.5<imc<24.99:
        print "Normal"
    elif 25<=imc:
        print "Sobre peso"
    elif 30<=imc:
        print "Obesidad morbida"
    elif 40<=imc:
        print "Obesidad morbida"
