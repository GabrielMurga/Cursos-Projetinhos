def converte_para_fahrenehit(celsius):
    return (celsius*9 + 160)/5
def converte_para_kelvin(celsius):
    return(celsius+273.15)
continuar="sim"
print("\n [CONVERSOR DE TEMPERATURA] \n")
while(continuar=="sim" or continuar=="s"):
    celsius=float(input("Informe a temperatura em C°: "))
    print("\n Escolha uma opção de conversão abaixo: ")
    print("[F] - Fahrenheit")
    print("[K] - Kelvin \n")
    opcao=input("\n Qual a sua opção[F/K]?? \n").upper()
    if(opcao=="F"):
        resultado=converte_para_fahrenehit(celsius)
        print("A temperatura em Fahrenheit é ",resultado,"F°")
    elif(opcao=="K"):
        resultado=converte_para_kelvin(celsius)
        print("A temperatura em Kelvin é" , resultado, "K")
    else:
        print("Opção invalida")
    continuar= input("\n Deseja continuar [sim/não]?").lower()

