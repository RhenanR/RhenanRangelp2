lista = [5, 8, 3, 24, 12, 9, 4]
if not lista:
    print("Lista vazia")
else:
    lista2 = lista[0]
    
    for num in lista:
        if num > lista2:
            lista2 = num
    
    print("O maior número na lista é: ", (lista2))