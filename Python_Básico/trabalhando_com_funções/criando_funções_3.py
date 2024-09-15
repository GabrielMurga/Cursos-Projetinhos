def calcular_fatorial(numero):
    fatorial=1
    for contador in range(1,numero+1):
        fatorial*= contador
    return fatorial
numero=int(input("\n Informe um numero inteiro qaulquer: "))
valor_fatorial=calcular_fatorial(numero)
print("O fatorial de ", numero, "é", valor_fatorial,"\n")  
if(valor_fatorial>100000):
    print("O valor do fatorial ultrapasssa 6 digitos ")  