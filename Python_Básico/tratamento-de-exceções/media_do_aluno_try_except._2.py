
print("\n[SITUAÇÃO DO ALUNO]")
errou=True
while(errou):
       try: 
        media = float(input("\nInforme a média do aluno: "))
        errou=False
       except:
        print("\n Você informou uma media errada, tente novamente") 
if(media>=7):
        print("\nO aluno está APROVADO\n")
else: 
     print("\nO aluno está REPROVADO\n")