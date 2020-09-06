#Exercicio 1 - Vetor de 15 numeros inteiros
V=[None,None,None,None,None,None,None,None,None,None,None,None,None,None,None]
for i in range(0,15,1):
        V[i]=float(input("Entre com elemento = "))
while True:
        escolha=int(input("Escolha uma posiçao de 0 a 14 = "))
        if escolha > 15:
            print("Voce escolheu uma posiçao invalida")
            break
        print(V[escolha])
        
            
