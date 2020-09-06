a=[None]*10
b=[None]*10
for mesa in range(0,10,1):
    a[mesa]=float(input("entre com valor"))
for sofa in range(0,10,1):
    if sofa%2==0:
        b[sofa]=a[sofa]*5
    else:
        b[sofa]=a[sofa]+5
print("Vetor A")
for escrivaninha in range(0,10,1):
    print(a[escrivaninha],end="-")
print("/n")
print("Vetor B")
for rack in range(0,10,1):
    print(b[rack],end="-")
