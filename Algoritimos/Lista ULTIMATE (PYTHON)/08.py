print("""
Exercicio 8:
Desenvolva um programa que receba dois valores, se o primeiro valor for maior que o segundo
exibir o dobro do primeiro valor digitado, caso contrário, exibir a metade do segundo valor.
""")

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

if valor1 > valor2:
    dobro = valor1 * 2
    print(f"O dobro do valor 1 é = {dobro}")

elif valor2 > valor1:
    metade = valor2 / 2
    print(f"A metade do valor 2 é = {metade}")

else:
    print("Não insira números iguais")