print("""
Exercicio 13:
Ler a idade de uma pessoa, informar se ela é estudante (1 para sim e 0 para não)
e ler o valor integral de um ingresso.

Pessoas com até 12 anos ou com 60 anos ou mais não pagam ingresso.
Estudantes com idade entre 13 e 59 anos pagam metade do valor.
As demais pessoas pagam o valor integral.

Valor do ingresso: R$ 50.00
""")

idade = int(input("Insira sua idade: "))
estudante = int(input("Você é estudante? (1 para sim e 0 para não): "))

ingresso = 50

isento = idade <= 12 or idade >= 60
metade = estudante == 1 and idade >= 13 and idade <= 59

if isento:
    print(f"Devido sua idade de {idade} anos você não paga ingresso. Bom filme!")

elif metade:
    desconto = ingresso / 2
    print(f"Você adquiriu o ingresso estudante.")
    print(f"O valor de R$ {ingresso:.2f} sai por R$ {desconto:.2f}. Bom filme!")

else:
    print(f"Você adquiriu o ingresso normal por R$ {ingresso:.2f}. Bom filme!")