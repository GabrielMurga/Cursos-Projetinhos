import os 
diretorio=os.path.dirname(os.path.realpath(__file__))
arquivo="mensagem.txt"
caminho= diretorio + "\\" + arquivo
def abrir_mensagem():
    print("[CONTEUDO DA MENSAGEM]")
    try:
        global caminho
        f=open(caminho,"r")
        conteudo=f.read()
        print(conteudo)
    except:
        print("Ops! Não foi possivel abir sua mensagem")
        print( "Voce previsa primeiro criar sua mensagem")
    input("\n Pressione [ENTER] para sair...")
def salvar_mensagem():
    print("[CRIANDO MENSAGEM] \n")
    mensagem=input("Digite a sua mensagem")
    try:
        global caminho
        f=open(caminho,"w")
        f.write(mensagem)
        f.close()
        print("\n Sua mensagem foi registrada com sucesso")
    except:
        print("Ops! Não foi possivel gravar mensagem no arquivo.")
        print("Arquivo e/ou diretorio protegido contra gravação")
        # inicio do progrma principal
continuar="sim"
print(" \n [GERENCIAR MENSAGEM] \n")   
while(continuar=="sim"or continuar=="s"):
    print("Escolha uma opção")
    print("[1]- Mostrar mensaem")
    print("[2]- Salvar mensagem")
    opcao=int(input("\n Qual a sua opção?[1/2]=>"))
    if(opcao==1):
         abrir_mensagem()
    elif(opcao==2):
        salvar_mensagem()
    else:
        print("Opção inválida!")
    continuar=input("Desejas continuar?[sim/nao]").lower()