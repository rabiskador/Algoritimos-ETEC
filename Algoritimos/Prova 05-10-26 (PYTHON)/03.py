print("""
Exercicio 3:
Leia:
- valor → valor de uma compra
- entrada → valor pago como entrada

Calcule o percentual da entrada em relação ao valor total:
percentual = (entrada / valor) * 100

Classifique a compra:
- Entrada menor que 20% → "Entrada baixa"
- Entrada entre 20% e 50% → "Entrada média"
- Entrada maior ou igual que 50% → "Entrada alta"

Além disso, calcule o valor que ficará para financiar.
""")


valor_compra = float(input("Coloque o valor da sua compra: "))
valor_entrada = float(input("Coloque o valor de entrada da sua compra: "))


percentual = (valor_entrada / valor_compra) * 100
financiamento = valor_compra - valor_entrada


if percentual < 20:

    print(f"Entrada baixa, você deu R$ {valor_entrada:.2f} "
          f"que vale cerca de {percentual:.1f}% "
          f"e ficou faltando R$ {financiamento:.2f} para financiar")


elif percentual >= 50:

    print(f"Entrada alta, você deu R$ {valor_entrada:.2f} "
          f"que vale cerca de {percentual:.1f}% "
          f"e ficou faltando R$ {financiamento:.2f} para financiar")


else:

    print(f"Entrada média, você deu R$ {valor_entrada:.2f} "
          f"que vale cerca de {percentual:.1f}% "
          f"e ficou faltando R$ {financiamento:.2f} para financiar")