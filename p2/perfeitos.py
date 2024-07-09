num=int(input("diga um número: "))
zero=(num)
div=0
lim=((num)+1)
for ordem in range(1, (lim)):
    if ((num)%(ordem)==0):
        div=((div)+(ordem))
    if ((ordem)==(num)):
        break
if (((div)-(zero))==(num)):
    print ("esse número é perfeito")
else:
    print ("esse número não é perfeito")