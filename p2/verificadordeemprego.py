nome=str(input("qual seu nome? "))
idade=int(input("qual a sua idade? "))
if(idade>=18):
    nacionalidade=str(input("de qual país você é? "))
    if(nacionalidade=="brasil"):
        experiencia=int(input("tem quantos anos de experiencia? "))
        if(experiencia>=2):
            print(nome, " você é habito para o trabalho")
        else:
            print("infelismente ",nome,"você não é habito ao trabalho")
    else:
        print("infelismente ",nome,"você não é habito ao trabalho")
else:
    print("infelismente ",nome,"você não é habito ao trabalho")