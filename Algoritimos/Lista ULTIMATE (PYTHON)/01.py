print("""
Exercicio 1:
As maças custam R$1.30/cada  se forem compradas menos de uma duzia, é R$1.00 se forem compradas >= 12
Escreva um algoritimo que leia o número
de maças compradas, calcule e escreva o custo total da compra
""")

quantidade = int(input("Digite a quantidade de maçãs compradas: "))

if quantidade >= 12:
    valor_total = quantidade * 1
    print(f"O valor a ser pago é de R$ {valor_total:.2f}")

else:
    valor_total = quantidade * 1.30
    print(f"O valor a ser pago é de R$ {valor_total:.2f}")