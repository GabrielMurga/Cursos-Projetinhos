lista_de_valores= ["Ana Claudia", 30, True, 6.5]

numero_total_itens_lista=len(lista_de_valores)

print("\n Total de itens na lista: ", numero_total_itens_lista, "\n")
print("Valores da lista")

for item in lista_de_valores:
    print(item)
print("\n Valor da primeira posição da lista ", lista_de_valores[0])

print("\n Valor da terceira posição da lista" , lista_de_valores[2])

if "Ana Claudia" in lista_de_valores:
    print("\n O nome Ana Claudia se encontra na lista\n")
else:
    print("O nome Ana Claudia não se encotra na lista")

lista_de_valores[1]= 50
lista_de_valores[3]= "Thiago Mello"
print("\n Valores da lista atualizados")
for item in lista_de_valores:
    print(item)