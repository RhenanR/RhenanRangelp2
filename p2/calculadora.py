nume1=float(input("qual o primeiro número da equação? "))
nume2=float(input("qual o segundo número da equação? "))
tipo=str(input("qual tipo de equação você deseja? "))
if ((tipo)== "soma"):
    print ((nume1)+(nume2))
elif ((tipo)== "subtracao"):
    print ((nume1)-(nume2))
elif ((tipo)== "divisao"):
    print ((nume1)/(nume2))
elif ((tipo)=="multiplicacao"):
    print ((nume1)*(nume2))
else:
    print ("erro")