#Programas prévia p1
print("Gabriel Coni Félix Reis, RA: 2160291912-047")

#Exercício 1
print("Exercício 1")
A=int(input("Digite o primeiro valor: "))
B=int(input("Digite o segundo valor: "))
soma=A+B
print("A soma dos valores é = ", soma)

#Exercício 2
print("Exercício 2")
s=float(input("Digite o seu salário = "))
if s > 1000:
    reaj=(5*s)/100
    s=s+reaj
    print("Reajuste de 5% = ", reaj)
    print("Seu novo salário é = ", s)
else:
    if s >= 500 and s <=1000:
        reaj=(10*s)/100
        s=s+reaj
        print("Reajuste de 10% = ", reaj)
        print("Seu novo salário é = ", s)
    else:
        if s < 500:
            reaj=(15*s)/100
            s=s+reaj
            print("Reajuste de 15% = ", reaj)
            print("Seu novo salário é = ", s)

#Exercício 3
print("Exercício 3")
a=int(input("Digite o primeiro valor = "))
b=int(input("Digite o segundo valor = "))
c=int(input("Digite o terceiro valor = "))
if a > b and b > c:
    print("O maior valor é = ", a)
else:
    if b > a and a > c:
        print("O maior número é = ", b)
    else:
        if c > b and b > a:
            print("O maior número é = ", c)

#Exercício 4
print("Exercício 4")
n=1
while n < 290:
      print(n)
      n=n+2

