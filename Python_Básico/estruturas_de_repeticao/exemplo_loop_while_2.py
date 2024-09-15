resposta="sim"
print("\n MOSTRANDO NOMES COMPLETOS \n")
while (resposta=="sim"):
    primeiro_nome=input("Digite o primeiro nome :")
    sobrenome=input("Digite o sobrenome :")
    print("Nome completo :", primeiro_nome, sobrenome, "\n")
    resposta= input("Deseja continuar[sim/não]?").lower()
print("Programa encerrado")    