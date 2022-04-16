"""  Faça um Programa que leia um número e exiba o dia correspondente da semana. 
1-Domingo, 2- Segunda, etc., se digitar outro valor deve
aparecer valor inválido"""
semana = int(input("Digite um número para saber o dia da semana correspondente:  " ))
if semana == 1:
    print(f"Você digitou o número {semana} que corresponde a Domingo. ")
elif semana == 2:
    print(f"Você digitou o número {semana} que corresponde a Segunda - feira. ")
elif semana == 3:
    print(f"Você digitou {semana} que corresponde a Terça - feira. ")
elif semana  == 4:
    print(f"Você digitou {semana} que corresponde a Quarta - feira.")
elif semana == 5:
    print(f"Você digitou {semana} que corresponde a Quinta - feira.")   
elif semana == 6:
    print(f"Você digitou {semana} que corresponde a Sexta - feira.")
elif semana == 7:
    print(f"Você digitou {semana} que corresponde a Sábado.")