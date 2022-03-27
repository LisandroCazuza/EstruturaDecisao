"""Faça um programa para a leitura de duas notas parciais de um aluno. 
O programa deve calcular a média alcançada por aluno e apresentar:
> A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
> A mensagem "Reprovado", se a média for menor do que sete;
> A mensagem "Aprovado com Distinção", se a média for igual a dez.  """
print("-"*66)
nota1 = float(input("Digite a primira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2 ) / 2
for media in range(0):
    if media > 10:
        print("A média ultrapassou 10 pontos!")
        break
    if media >= 7:
        print(f"Aprovado com média: {media} pontos.")
    if media < 7:
        print(f"Reprovado com média: {media} pontos. ")
    if media == 10:
        print(f"Aprovado com Distinção sua média é: {media} pontos")
    
    





