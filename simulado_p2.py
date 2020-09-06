def matriz_a(n):
   a=[]
   total=0
   while True:
       elem=int(input("entre com elemento = "))
       if total==n:
         break
       if elem%2==0:
            a.append(elem)
            total=total+1
       else:
            print("só aceita par")
   return a

def matriz_b(n):
    b=[]
    total=0
    while True:
        elem=int(input("entre com elemento = "))
        if total==n:
            break
        if elem%2==0:
            print("so aceita impar")
        else:
            b.append(elem)
            total=total+1
    return b

def matriz_c(n,p):
    c=[]
    for i in n:
        c.append(i)
    for i in p:
        c.append(i)
    return c	

def ordem_crescente(L):
    L=[None]*10
    total=0
    while True:
        elem=int(input("entre com elemento = "))
        if total==L:
            break
        print ("him")

        
class Televisao:
    def __init__(self):
        self.ligada=False
        self.canal=2
def muda_canal_para_baixo(self):
    self.canal=canal-1
def muda_canal_para_cima(self):
    self.canal=canal+1

#criar um método que ligue e desligue a tv

def liga_desliga(self,a):
        if a=="liga":
            self.ligada=True
        elif a=="desliga":
            self.ligada=False
        else:
            print("Opção invalida")



#funçoes
#len() = retorna o tamanho da lista

#lista.append(valor) = acrescenta o valor ao final da lista
#range(inicio,final,incremento)=constroi uma lista do inicio ao final seguindo o incremento  

#Busca binaria recursiva
def binary_search_rec(vet, num, esq, dir, tentativa):
	meio = (esq + dir) // 2
	aux_num = vet[meio]
	if num == aux_num:
		return tentativa
	elif num > aux_num:
		return binary_search_rec(vet, num, meio, dir, tentativa + 1)
	return binary_search_rec(vet, num, esq, meio, tentativa + 1)
