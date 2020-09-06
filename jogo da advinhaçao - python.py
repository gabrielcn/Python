#Jogo da Advinhação
print("JOGO DA ADVINHAÇAO")
print("Escolha um número de 0 a 10")
while chances > 0:
chute=int(input("Escolha algum número = "))
numerosecreto=6
if chute == numerosecreto:
    print("Parabéns vc acertou")
else:
    if chute > numerosecreto:
        print("vc errou, o número secreto é menor")
    else:
        print("vc errou, o número secreto é maior")
        


