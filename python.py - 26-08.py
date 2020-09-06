#Aula de hoje Python - 26/08
'''
print("Hello World")
graca=input("Entre com seu nome = ")
print("Seu nome é", graca)

#Ex1 Programa Volume de uma Caixa
c=float(input("Informe comprimento = "))
a=float(input("Informe altura = "))
p=float(input("Informe profundidade = "))
v=c*a*p
print("apresentar resultado = ",v)

#Ex2 Programa volume de uma lata
r=float(input("Informe o raio = "))
a=float(input("Informe a altura = "))
vol=(r*r)*a*3.14
print("Volume da lata = ", vol)

#Ex3 Litro de combustivel comsumido
t=float(input("Informe o tempo gasto = "))
vm=float(input("Informe a velocidade media = "))
lc=t*vm
print("Litros de combustivel gasto na viagem = ", lc)

#Ex4 Valores maiores que 10
n=float(input("Informe o numero = "))
if n > 10:
    print("numero maior que 10")
    
#Ex5 Valores maiores que 5
n=float(input("Informe o numero = "))
if n > 5:
    print("maior que 5")
else:
    print("menor que 5")
'''
#Ex6 Programa faixa salarial
s=float(input("Informe o seu salario"))
if s < 500:
    sl=s*15/100
    s=sl+s
    print("Seu novo salario é = ", s)
else:
    if s >= 500 and s < 1000:
     sl=s*10/100
     s=sl+s
     print("Seu novo salario é = ", s)
    else:
     sl=s*5/100
      s=sl+s
      print("Seu novo salario é = ", s)
    
