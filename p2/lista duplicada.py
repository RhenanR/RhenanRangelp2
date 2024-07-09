lista=[1, 2, 3, 3, 4, 5, 5]
lista2=[]
for iten in lista:
    if iten not in lista2:
        lista2.append(iten)
print (lista2)