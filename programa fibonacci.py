#Fibonacci
atual=0
anterior=1
proximo=1
while atual<377:
    proximo=anterior+atual
    print(proximo)
    anterior=atual
    atual=proximo
