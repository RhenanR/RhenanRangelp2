fila=["fulano", "ciclano", "alguem", "cliente", "pessoa", "humano"]
print (fila)
for pessoa in range (1,50):
    pessoa=str(input("quem entrou na fila? "))
    fila.append(pessoa)
    if ((pessoa)=="fim"):
        fila.pop(0)
        break
print (fila)