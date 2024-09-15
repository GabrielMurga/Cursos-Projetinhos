continuar="sim"
clientes=[]
print("\n [CADASTRO DE CLIENTES]")
while(continuar == "sim" or continuar == "s"):
    nome_cliente=input("\n Informe o nome do cliente: ")
    clientes.append(nome_cliente)
    continuar=input("Deseja continuar [sim/não]?").lower()
print(" \n Lista de clientes cadastrados \n ")
for cliente in clientes:
    print(cliente)