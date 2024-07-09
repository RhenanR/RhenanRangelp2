qnt=int(input("quantos números pertencente a sequencia você quer? "))
conta=4
f1=int(1)
f2=int(1)
if qnt>0:
    print(0)
if qnt>1:
    print (f1)
if qnt>2:
    print(f2)
fn=(f1+f2)
while (conta<=qnt):
    fn=(f1+f2)
    print (fn)
    f1=int(f2)
    f2=int(fn)
    conta=conta+1