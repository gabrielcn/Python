import random
print("*******************")
print("jogo da adivinhação")
print("*******************")
numero_secreto=random.randrange(1,10,1)
a=1
while a<4:
    print("Chance numero",a)
    chute=int(input("Digite seu numero \n  "))
    if numero_secreto==chute:
        print("Parabéns vc acertou")
        break
    elif numero_secreto>chute:
        print("Vc errou, o numero secreto é maior.")
    elif numero_secreto<chute:
        print("Vc errou, o numero secreto é menor.")
    a=a+1
print("fim do programa")
