#Exemplo em que iremos depurar a execução de um código passo a passo

numero = int(input("Informe um número inteiro: "))

fatorial = 1

for contador in range(1,numero + 1):
    fatorial *= contador

print("O fatorial de ",numero," é ", fatorial)