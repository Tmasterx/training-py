import random

str(input("deseja começar o experimento? s/n: "))

if "s"or"S":
    print("vamos começar o experimento\n ")

    nome=str(input("qual é o seu nome? "))

    print(f"{nome},voce esta testando um experimento  de alguem que está aprendendo a programar,então se prepare para o que vem por ai\n")

    idade=int(input("para começar quero saber mais sobre voce,qual é a sua idade?  "))

    if idade >=18:
        print(f"ja imaginava, afinal o nome {nome} combina com a sua idade\n   ")
        
        x=random.randint(1,10)

        y=random.randint(20,30)

        z= x*y

        print(f"agora vamos testar seus conhecimentos,me fale quanto é {x} vezes {y}?\n")

        resposta=int(input("resposta:"))
        if resposta ==z:
            print("seu intelecto me impressiona, parabens você acertou")
        else:
            print(f"sinto muito, a resposta certa é {z}")
    else:
        print("realmente seu nome tem a aura de alguem jovem \n")

        x=random.randint(1,10)

        y=random.randint(1,10)

        z= x*y

        print(f"vamos ver se voce tem aura+ego, me fale quanto é {x} vezes {y}?  ")

        resposta=int(input("resposta:"))
        if resposta ==z:
            print("sua aura e ego são muito fortes,vc acertou!")

        else:
                print(f"sua aura e ego são fracos, a resposta certa é {z}")                    
    
else:
    print("falou")    