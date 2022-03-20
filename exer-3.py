"""   3.Faça um Programa que verifique se uma letra digitada é "F" ou "M" ou "H". 
Conforme a letra escrever: F - Feminino, M - Masculino ou H - Homossexual"""

sexualidade = input("Digite sua sexualidade -F - Feminino, M - Masculino ou H - Homossexual - :  ").title()
if sexualidade == 'F':
    print(f" Foi digitado  {sexualidade} portanto você é feminina.")
if sexualidade == 'M':
    print(f" Foi digitado  {sexualidade} portanto você é masculino.")
if sexualidade == 'H':
    print(f" Foi digitado  {sexualidade} portanto você é homossexual.")
else:
    print("Não foi digitado nenhuma das opções. Desta forma não há regitro de sexualidade")
