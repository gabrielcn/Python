#Programa Renda
RND=float(input("Informe Renda"))
if RND>15.760:
    print("Classe A")
else:
    if RND>7.880:
        print("Classe B")
    else:
        if RND>3.152:
            print("Classe C")
        else:
            if RND>1.576:
                 print("Classe D")
            else:
                    print("Classe E")
                
