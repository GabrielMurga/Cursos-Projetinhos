def calcular_bonus_A(salario_funcionario):
    return (salario_funcionario*0.05)
def calcular_bonus_B(salario_funcionario):
    return(salario_funcionario*0.1)
    
continuar="sim"
while(continuar=="sim" or continuar=="s"):
    nome_funcionario=input("Informe o nome do funcionário: ")
    salario_funcionario=float(input("Informe o salário do funcionario: "))
    nivel_funcionario=input("Informe o nivel do funcionário [A/B]: ").upper()
    if (nivel_funcionario=="A"):
        bonus_total=calcular_bonus_A(salario_funcionario)
    elif(nivel_funcionario=="B"):
        bonus_total=calcular_bonus_B(salario_funcionario)
    print("\n [DADOS DO FUNCIONARIO] \n")
    print("Nome: ",nome_funcionario)
    print("Salario: ",salario_funcionario)
    print("Nivel: ",nivel_funcionario)
    print("Bonus: ",bonus_total)
    continuar=input("Desejas calcular o bônus de outro funcionário? ").lower()

