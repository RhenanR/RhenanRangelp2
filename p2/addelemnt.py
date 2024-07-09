fila=[]
for itens in range(1, 2001):
    cd=input("quais itens você deseja adicionar a lista? ")
    fila.append(cd)
    if ((cd)=="parar"):
        fila.pop(-1)
        break
print (fila)