print ("""
Desafio 01 — Preço com desconto
Leia o valor de uma compra.

Se o valor for igual ou superior a R$ 200,00, aplique um desconto de 10%.
Caso contrário, não aplique desconto.
Ao final, mostre o valor do desconto e o valor final da compra.
""")

compra = float(input("Digite o valor da compra: R$ "))

if compra >= 200:
    desconto = compra * 0.10

else:
    desconto = 0

valor_total = compra - desconto

print(f"Valor da compra: R$ {compra:.2f}")
print(f"Valor do desconto: R$ {desconto:.2f}")
print(f"Valor final: R$ {valor_total:.2f}")
