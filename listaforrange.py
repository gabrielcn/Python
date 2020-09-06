#pag137ex1
md=[None]*8
for mesa in range(0,8,1):
    md[mesa]=float(input("entre com valor = "))
soma=0
for cadeira in range(0,8,1):
    soma=soma+md[mesa]
print("A soma é: ", soma)
