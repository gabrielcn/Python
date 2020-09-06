#Programa Bhaskara
a=int(input("Informe valor de a"))
b=int(input("Informe valor de b"))
c=int(input("Informe valor de c"))
D=(b*b)-4*a*c
if D>0:
    print(D)
    x1=-b+(D**(1/2))/2*a
    print("Valor x1",x1)
    x2=-b -(D**(1/2))/2*a
    print("Valor x2",x2)
else:
    if D==0:
        print(D)
        x1=-b/2*a
        print("Valor da raiz",D)
    else:
        print("Nao existe soluçao real")
