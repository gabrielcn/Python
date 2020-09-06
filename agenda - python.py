#programa agenda
agenda=["Nome: ","Endereço: ","Código Postal: ","Bairro: ","Telefone: "],[None,None,None,None,None],[None,None,None,None,None],[None,None,None,None,None],[None,None,None,None,None],[None,None,None,None,None],
for i in range(1,11,1):
    for j in range(0,5,1):
        agenda[i][j]=input("Informe Nome: ")
        agenda[i][j]=input("Informe Endereço: ")
        agenda[i][j]=input("Informe Código Postal: ")
        agenda[i][j]=input("Informe Bairro: ")
        agenda[i][j]=input("Informe Telefone: ")
        break
for i in range(1,11,1):
    for j in range(0,5,1):
        print("Nome: ",agenda[i][j])
        print("Endereço: ",agenda[i][j])
        print("Código Postal: ",agenda[i][j])
        print("Bairro: ",agenda[i][j])
        print("Telefone: ",agenda[i][j])
        
