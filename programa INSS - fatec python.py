#Programa INSS
S=float(input("Informe o salário"))
if S<=1751.82:
    INSS=(S*5)/100
    print("INSS =",INSS)
else:
    if S<=2819.72:
        INSS=(S*9)/100
        print("INSS =",INSS)
    else:
        if S<=5839.46:
            INSS=(S*11)/100
            print("INSS =",INSS)
        else:
            print("INSS = 643")
            
