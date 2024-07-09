x=(float(input("diga um número e eu direi se é primo ")))
if (x==1):
    print ("esse número não é primo")
elif (x%2==0) and (x!=2):
    print ("esse número não é primo")
elif(x%3==0) and (x!=3):
    print ("esse número não é primo")
elif(x%7==0) and (x!=7):
    print ("esse número não é primo")
elif(x%5==0) and (x!=5):
    print ("esse número não é primo")
else:
    print ("esse número é primo")