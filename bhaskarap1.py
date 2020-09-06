#Bhaskara P1
a=float(input("Entre com valor de a = "))
b=float(input("Entre com valor de b = "))
c=float(input("Entre com valor de c = "))
D=(b*b)-4*a*c
if D > 0:
    print (D)
    x1 = -b+ (D**(1/2))/2*a
    print("Valor x1 = ", x1)
    x2 = -b- (D**(1/2))/2*a
    print("Valor x2", x2)
else:
    if D == 0:
        print(D)
        x1=-b/2*a
        print("Valor de uma raíz = ", x1)
    else:
        print("Não existe solução real")
