import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
salario_bruto=float(input("Digite salario bruto: "))
numero_filhos=int(input("Informe o numero de filhos: "))
bonus= (salario_bruto * 0.05)
salario_familia= (numero_filhos*27.64)
inss= (salario_bruto*0.08)
vale_trasporte=(salario_bruto*0.06)
salario_liquido= (salario_bruto + bonus + salario_familia - inss - vale_trasporte)
print( "O salario liquido é de ",locale.currency( round(salario_liquido,2)))
#Outros valores
print("Bonus: " ,locale.currency(bonus))
print("Salario familia", locale.currency(salario_familia))
print("INSS" , locale.currency(inss))
print("Vale transporte", locale.currency( vale_trasporte))