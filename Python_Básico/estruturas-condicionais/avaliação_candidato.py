nota_candidato=float(input("Informe a nota do candidato: "))
print("Nota do candidato", nota_candidato)
if(not nota_candidato >= 8):
    print("O candidato está reprovado")
else:
    print("O candidato está aprovado")