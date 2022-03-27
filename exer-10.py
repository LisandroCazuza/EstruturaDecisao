"""Faça um Programa que pergunte em que turno você estuda. 
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a
mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso."""
print("-"*50)
turno = input("Em qual turno você estuda?  ").title()
if turno == 'M':
    print("Bom Dia! Estudante!")
if turno == 'V':
    print("Boa Tarde! Estudante!")
    if turno == 'N':
        print("Boa Noite! Estudante!")
    else:
        print("Valor Inválido!Estudante!")