nome_candidato= input("Informe o nome do candidato :")
notaTesteTeorico=float(input("Informe a nota do candidato no teste teorico :"))
notaTestePratico=float(input("Informe a nota do canditado no teste pratico :"))
print("Candidato: ", nome_candidato)
print("Nota do teste teorico: " , notaTesteTeorico)
print(" Nota do teste pratico: " , notaTestePratico)
if(notaTesteTeorico >= 8 or notaTestePratico>=9):
    print("O candidato",nome_candidato,"poderá concorrer a vaga ")
else:
    print("O candidato", nome_candidato, "não poderá concorrer a vaga")