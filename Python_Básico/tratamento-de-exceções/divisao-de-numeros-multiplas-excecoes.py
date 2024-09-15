#Neste programa será feita a divisão entre dois números
#Aqui várias exceções diferentes podem acontecer
try:
    print("\n[DIVISÃO ENTRE DOIS NÚMEROS]\n")
    numero1 = float(input("Informe o primeiro número:"))
    numero2 = float(input("Informe o segundo número:"))
except ValueError:
    print("O valor que você informou está invalido, não é possível dividir ")
except ZeroDivisionError:
    print("Não existe divisão de qualquer número por 0")

resultado = numero1 / numero2

print("\nRESULTADO: ", resultado,"\n")
