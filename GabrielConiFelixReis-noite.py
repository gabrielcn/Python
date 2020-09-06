print("Gabriel Reis - RA: 2160291912047")
print("---------------------------------")
print("Exercício 1")
a=int(input("Digite o número da letra a = "))
b=int(input("Digite o número da letra b = "))
soma=a+b
print("O valor da soma é = ", soma)
print("------------------------------------")
print("Exercício 2")
s=float(input("Digite seu salário = "))
if s > 1000:
    s1=(s*5)/100
    s=s + s1
    print("Reajuste de 5% = ",s1)
    print("O seu novo salário é = ",s)
else:
    if s <= 1000 and s >= 500:
        s1=(s*10)/100
        s=s + s1
        print("Reajuste de 10% = ",s1)
        print("O seu novo salário é = ",s)
    else:
        if s < 500:
            s1=(s*15)/100
            s=s + s1
            print("Reajuste de 15% = ",s1)
            print("O seu novo salário é = ",s)
print("---------------------------------------")
print("Exercício 3")
a=int(input("Digite o valor de a = "))
b=int(input("Digite o valor de b = "))
c=int(input("Digite o valor de c = "))
if a > b and a > c:
    print("O maio número é = ",a)
else:
    if b > a and b > c:
        print("O maior número é = ",b)
    else:
        if c > a and c > b:
            print("O maior número é = ",c)
print("-------------------------------------")
print("Exercício 4")
var = 1
while var < 290:
    print(var)
    var = var + 2
            
        
