#Faz a leitura da média do aluno, com tratamento de exceções try/except
try:
    print("\n[SITUAÇÃO DO ALUNO]")
    media = float(input("\nInforme a média do aluno: "))

    if(media>=7):
        print("\nO aluno está APROVADO\n")
    else: 
     print("\nO aluno está REPROVADO\n")
except:
    print("Você informou uma média invalida \n")