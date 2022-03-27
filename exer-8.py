"""Faça um programa que pergunte o preço de três produtos e informe
qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato."""
print("-" * 50)
p1 = input("Digite o nome do produto: ")
n1 = float(input("Digite o primeiro valor: "))
p2 = input("Digite o nome do produto: ")
n2 = float(input("Digite o segundo valor: "))
p3 = input("Digite o nome do produto: ")
n3 = float(input("Digite o terceiro valor: "))
if n1 < n2 and n1 < n3:
    print(f"O valor do produto 1:  R$ {n1} {p1} é o mais barato. ")
if n2 < n1 and n2 < n3:
    print(f"O valor do produto 2:  R$ {n2} {p2} é o mais barato. ")
if n3 < n1 and n3 < n2:
    print(f"O valor do produto 3:  R$ {n3} {p3} é o mais barato. ")
