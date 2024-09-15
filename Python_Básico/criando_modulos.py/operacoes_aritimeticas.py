import matematica as m
print("\n [OPERAÇÕES ARITMETICAS]")
continuar="sim"
while(continuar == "sim"):
    num1=float(input("\n Informe o primeiro numero: "))
    num2=float(input("Informe o segundo numero: "))
    print("\nEscolha uma das opções abaixo: \n")
    print("[1] - Adição")
    print("[2] - Subtração")
    print("[3] - Multiplicação")
    print("[4] - Divisão")
    opcao=int(input("\n Qual a sua opção? [1-4]?"))
    if(opcao==1):
        resultado= m.somar_numeros(num1,num2)
        print("Soma:",resultado)
    elif(opcao==2):
        resultado= m.subtrair_numeros(num1,num2)
        print("Subtração",resultado)
    elif(opcao==3):
        resultado=m.multiplicar_numeros(num1,num2)
        print("Multiplicação",resultado)
    elif(opcao==4):
        resultado=m.dividir_numeros(num1,num2) 
        print("Divisão",resultado)
    else:
        print("\n Opção invalida...")
    continuar=input("\n Desejas continuar.[sim/não]?").lower()