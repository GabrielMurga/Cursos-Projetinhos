itens_da_tupla= ("Ana Claudia", 30,True, 6.5)
total_itens_tupla=len(itens_da_tupla)
print("\n Total de itens da tupla", total_itens_tupla, "\n")
print("\n Valores da tuplar : ", itens_da_tupla)
print("\n Valor da segunda posição da tupla : ", itens_da_tupla[1])
print("\n Valor da terceira posição da tupla : ", itens_da_tupla[2])
if "Ana Claudia" in itens_da_tupla:
    print("o nome Ana CLaudia esta na lista")
else:
    print("O nome nao esta na lista ")
    #Perceba que pode indicar o valor da tupla sem necessidade de criar um loop (for)
    # Para imprimir os valores um embaixo do outro é necessario utilizar a estrutura do for 
    