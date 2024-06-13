turma=[]
for nome in range (1,30):
    nome=str(input("um nome de um aluno: "))
    turma.append(nome)
    if ((nome)=="fim"):
        turma.pop(-1)
        break
print (turma)