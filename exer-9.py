"""Faça um Programa que leia três números e mostre-os em ordem decrescente."""
print("-" * 50)
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
if n3 < n2 and n2 < n1:
    print(f"Ordem decrescente n3: {n3} , n2: {n2} e n1: {n1}")
if n2 < n1 and n1 < n3:
    print(f"Ordem decrescente n2: {n2} , n1: {n1} e n1: {n3}")
if n1 < n2 and n2 < n3:
    print(f"Ordem decrescente n1: {n1} , n2: {n2} e n3: {n3}")
if n3 < n1 and n1 < n2:
    print(f"Ordem decrescente n3: {n3} , n1: {n1} e n2: {n2}")
if n2 < n3 and n3 < n1:
    print(f"Ordem decrescente n2: {n2} , n3: {n3} e n1: {n1}")
if n1 < n3 and n3 < n2:
    print(f"Ordem decrescente n1: {n1} , n3: {n3} e n2: {n2}")
