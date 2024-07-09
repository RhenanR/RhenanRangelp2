fila1=[]
fila2=[]
for iten1 in range (1, 2001):
    iten1=input("o que colocar na fila 1? ")
    fila1.append(iten1)
    if ((iten1)=="nada"):
        fila1.pop(-1)
        break
for iten2 in range (1, 2001):
    iten2=input("o que colocar na fila 2? ")
    fila2.append(iten2)
    if ((iten2)=="nada"):
        fila2.pop(-1)
        break
filaFINAL=(fila1)+(fila2)
print (filaFINAL)
for letras in filaFINAL:
    print (letras)