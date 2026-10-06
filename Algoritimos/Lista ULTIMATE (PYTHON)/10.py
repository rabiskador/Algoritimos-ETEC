print("""
Exercicio 10:
Desenvolva um algoritmo que receba a idade em anos e a altura em metros de um usuário.
O usuário somente pode participar da montanha russa se tiver pelo menos 12 anos
e 1.30 de altura.
Exibir para o usuário se ele pode ou não andar na montanha russa.
""")

idade = int(input("Insira sua idade: "))
altura = float(input("Insira sua altura em metros: "))

liberado = idade >= 12 and altura >= 1.30

if liberado:
    print("Você está liberado para andar na montanha russa")
else:
    print("Você não pode andar na montanha russa")