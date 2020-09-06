def matriz_a(n):
    a=[]
    total=0
    while True:
        elem=int(input("entre com elemento ==>"))
        if total==n:
            break             
        if elem%2==0:
            a.append(elem)
            total=total+1
        else:
            print("só aceita par")
    return a

#construindo a função matriz_b(): Constroi uma matriz com valores impares. A quantidade de elementos é determinada pela matriz a

def matriz_b():
    b=[]
    total=0
    n=len(a)
    while True:
        elem=int(input("entre com elemento ==>"))
        if total==n:
            break             
        if elem%2!=0:
            b.append(elem)
            total=total+1
        else:
            print("só aceita impar")
    return b
for in range(0, n, 1):

#refazer a função matriz_c
#construindo a função matriz_c(): Constroi uma matriz com valores da junção de matriz a com matriz B

def matriz_c(n,):
    c=[]
    for i in n:
        c.append(i)
    for i in p:
        c.append(i)
    return c	
