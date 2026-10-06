print("""
Exercício 9:
Desenvolva um programa que receba 4 valores,
exiba a soma dos dois maiores valores!
""")

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))
valor4 = float(input("Digite o quarto valor: "))

maior = valor1
segundo = valor2

if valor2 > maior:
    maior = valor2
    segundo = valor1

if valor3 > maior:
    segundo = maior
    maior = valor3

elif valor3 > segundo:
    segundo = valor3

if valor4 > maior:
    segundo = maior
    maior = valor4

elif valor4 > segundo:
    segundo = valor4

print(f"A soma dos dois maiores valores é {maior + segundo}")