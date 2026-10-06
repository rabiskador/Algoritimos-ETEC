print("""
Desafio 03 — Cálculo da média
Leia três notas de um aluno e calcule a média aritmética.

Mostre uma das mensagens:

Média igual ou superior a 7: Aprovado
Média entre 5 e 6,9: Recuperação
Média menor que 5: Reprovado
Mostre também a média calculada.
""")



n1 = float(input("Insira sua primeira nota: "))
n2 = float(input("Insira sua segunda nota: "))
n3 = float(input("Insira sua terceira nota: "))

media = (n1 + n2 + n3) / 3

if media >= 7:
    situacao = "Aprovado"

elif media >= 5:
    situacao = "Recuperação"

else:
    situacao = "Reprovado"

print(f"Sua média foi {media:.2f}")
print(f"Situação: {situacao}")
