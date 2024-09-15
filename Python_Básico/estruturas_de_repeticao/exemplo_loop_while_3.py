numero=int(input("informe um número inteiro :"))
fatorial= 1
contador= 1
while(contador <= numero):
    fatorial = fatorial * contador
    contador+=1
print("O fatorial de ", numero,"é" , fatorial)