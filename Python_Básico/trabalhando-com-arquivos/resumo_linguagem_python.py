import os
diretorio=os.path.dirname(os.path.realpath(__file__))
arquivo="resum.txt"
caminho= diretorio +"\\"+ arquivo
print("\n [Resumo da linguagem Python] \n")
try:
    f=open(caminho,"r",encoding="utf-8")
    conteudo= f.read()
    print(conteudo)
    input("\n Pressione [ENTER] para encerrar \n")
except:
    print("Ops! Não foi possivel abrir o arquivo.")
    print("Ele nao se encontra na pasta.\n")