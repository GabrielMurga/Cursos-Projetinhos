contagem=1
numeros=[]
while(contagem<=10):
    numero_pedido= float(input("Informe o número :"))
    numero_pedido *= 3
    numeros.append(numero_pedido)
    contagem+=1
print("\n[LISTA DOS NUMEROS ESCOLHIDOS]\n")
for numero in numeros:
    print(numero)