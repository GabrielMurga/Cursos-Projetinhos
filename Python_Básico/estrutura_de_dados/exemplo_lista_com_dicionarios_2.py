clientes=[]
resposta="sim"
print("\n [CADASTRO DE  CLIENTES]")
while(resposta=="sim"):
    nome_cliente=input("\n Informe o nome do cliente: ")
    telefone_cliente= input("Informe o telefone do cliente: ")
    email_cliente= input("Informe o emmail do cliente:  ")
    dados_cliente={"nome": nome_cliente, "telefone": telefone_cliente, "email":email_cliente}
    clientes.append(dados_cliente)
    resposta=input("\n Deseja continuar? [sim/não]").lower()
print("\n \n [LISTA DE CLIENTES CADASTRADOS]")
for cliente in clientes:
    print("Nome :", cliente["nome"] )
    print("Telefone :", cliente["telefone"] )
    print("Email :", cliente["email"])
input("Pressione [ENTER] para sair....")