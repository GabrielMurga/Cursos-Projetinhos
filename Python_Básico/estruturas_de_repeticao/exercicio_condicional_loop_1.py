contagem=1
numeros=[]
menor_numero=int(input("Informe um número inteiro: "))
while(contagem<=9):
    numero_informado=int(input("Informe um número inteiro: "))
    numeros.append(numero_informado)
    if (numero_informado<menor_numero):
        menor_numero=numero_informado
    contagem+=1
print(menor_numero)

