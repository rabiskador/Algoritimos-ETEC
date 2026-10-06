print("""
Desafio 07 — Sistema de desconto para compras

Leia o valor da compra, se a pessoa possui cartão da loja e se é estudante.

Regras:
- Se a pessoa possuir cartão da loja ou for estudante, receberá 10% de desconto.
- Caso contrário, não haverá desconto.
""")

valor_compra = float(input("Digite o valor da compra: "))

cartao = input("Possui cartão da loja? ").strip().lower()
estudante = input("É estudante? ").strip().lower()

tem_cartao = cartao == "sim" or cartao == "s"
eh_estudante = estudante == "sim" or estudante == "s"

if tem_cartao or eh_estudante:
    valor_final = valor_compra * 0.90
    print(f"Valor final: R$ {valor_final:.2f}")
    print("Desconto de 10% aplicado.")

else:
    print(f"Valor final: R$ {valor_compra:.2f}")
    print("Nenhum desconto foi aplicado.")
