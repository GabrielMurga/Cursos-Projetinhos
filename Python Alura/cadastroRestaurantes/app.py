import os
restaurantes=[{'nome': 'Bobs','categoria':'Lanche','situacao':False} 
               ,{'nome': 'ShushiRJ','categoria':'Japonesa','situacao':False}]

def exibir_nome():
    print("""
        

    ████████╗░█████╗░░█████╗░██╗░░░██╗███╗░░░███╗███████╗░█████╗░███╗░░░███╗███████╗
    ╚══██╔══╝██╔══██╗██╔══██╗██║░░░██║████╗░████║██╔════╝██╔══██╗████╗░████║██╔════╝
    ░░░██║░░░██║░░██║██║░░╚═╝██║░░░██║██╔████╔██║█████╗░░██║░░██║██╔████╔██║█████╗░░
    ░░░██║░░░██║░░██║██║░░██╗██║░░░██║██║╚██╔╝██║██╔══╝░░██║░░██║██║╚██╔╝██║██╔══╝░░
    ░░░██║░░░╚█████╔╝╚█████╔╝╚██████╔╝██║░╚═╝░██║██║░░░░░╚█████╔╝██║░╚═╝░██║███████╗
    ░░░╚═╝░░░░╚════╝░░╚════╝░░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░░░░░╚════╝░╚═╝░░░░░╚═╝╚══════╝   
            """)

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)

def voltar_menu():
    input("Digite uma tecla para voltar para o menu: ")
    main()

def cadastra_restaurante():
    exibir_subtitulo("Bem vindo à area de cadastro de restaurantes\n")
    nome_restaurante= input("Diga o nome do restaurante que desejas cadastrar: \n")
    categoria= input( f"Diga a categoria na qual o {nome_restaurante} se encaixa:\n ")
    dados_coletados={'nome': nome_restaurante,'categoria':categoria,'situacao':False }
    restaurantes.append(dados_coletados)
    print(f"Cadastro do restaurante {nome_restaurante} realziado com sucesso ")
    voltar_menu()

def exibe_restaurantes():
    exibir_subtitulo("Lista de restaurantes cadastardos\n")
    print(f"{'Nome do restaurante'.ljust(20)}|| {'Categoria'.ljust(20)}||{'Status'}\n")
    for restaurante in restaurantes:
        nome_restaurante=restaurante['nome']
        categoria=restaurante['categoria']
        situacao= 'Ativado' if restaurante['situacao'] else 'Desativado'
        print(f'{nome_restaurante.ljust(20)}||{categoria.ljust(20)}||{situacao}')
    voltar_menu()

def exibir_opcoes():
    print('1. Cadastrar retaurante')
    print('2. Listar restaurente')
    print('3. Alterar situação do restaurente')
    print('4. Sair')

def finaliza_app():

  exibir_subtitulo("Finalizar Programa")

def opcao_invalida():
    print("Opção Inválida\n")
    input("Pressione qualquer tecla para voltar ao início do programa: ")
    main()

def mudar_situacao():
    exibir_subtitulo("Mudando a situação do restaurante\n")
    nome_restaurante=input("Digite o nome do restaurante que desejas mudar a situação: ")
    restaurante_encontrado=False
    for restaurante in restaurantes:
        if nome_restaurante==restaurante['nome']:
            restaurante_encontrado= True
            restaurante['situacao']= not restaurante['situacao']
            print(f"A situaçao do {nome_restaurante} foi alterada com sucesso\n")
            
    if not restaurante_encontrado:
        print("Restaurante não encontrado\n")
    voltar_menu()

def escolher_opcao():
    try:
        opcao_escolhida= int(input('\nEscolha uma opçao: '))
        if (opcao_escolhida==1):
            cadastra_restaurante()
        elif (opcao_escolhida==2):
            exibe_restaurantes()
        elif (opcao_escolhida==3):
            mudar_situacao()
        elif (opcao_escolhida==4):
            finaliza_app
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome()
    exibir_opcoes()
    escolher_opcao()
if (__name__=='__main__'):
    main()