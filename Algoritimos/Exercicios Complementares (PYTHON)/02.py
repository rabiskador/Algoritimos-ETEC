print("""
Desafio 02 — Classificação de idade
Leia a idade de uma pessoa e mostre sua classificação:

De 0 a 12 anos: Criança
De 13 a 17 anos: Adolescente
De 18 a 59 anos: Adulto
60 anos ou mais: Idoso
Considere que a idade informada será um valor válido.
""")

idade = int(input("Digite sua idade: "))

if idade >= 60:
    classificacao = "Idoso"


elif idade >= 18:
    classificacao = "Adulto"


elif idade >= 13:
    classificacao = "Adolescente"


else:
    classificacao = "Criança"

print(f"Idade: {idade} anos")
print(f"Classificação: {classificacao}")
