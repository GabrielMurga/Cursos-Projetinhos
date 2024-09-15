print("PROGRAMA TABUADA EM PYTHON \n")
numero=int(input("Informe um número :"))
contador=1
print("\n Tabuada do numero: " , numero, "\n")
while(contador<=10):
    resultado=(contador*numero)
    print(numero , "x", contador, "=" , resultado)
    contador+=1 