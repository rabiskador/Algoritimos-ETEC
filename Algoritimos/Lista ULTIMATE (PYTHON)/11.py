print("""
Exercicio 11:
Desenvolva um algoritmo que receba três notas, a quantidade de aulas e a quantidade de faltas,
sabendo que para ser aprovado deve ter média maior que 5 e frequência maior que 75%.
Exiba se o aluno foi aprovado ou reprovado junto à média e frequência.
""")

quantidade_aulas = int(input("Digite a quantidade de aulas que teve: "))
quantidade_faltas = int(input("Digite quantas aulas você faltou: "))

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

frequencia = 100 - (quantidade_faltas / quantidade_aulas * 100)
media = (nota1 + nota2 + nota3) / 3

aprovado = media > 5 and frequencia > 75

if aprovado:
    print(f"Parabéns, você foi aprovado! Sua média foi {media:.1f} e sua frequência foi {frequencia:.1f}%")
else:
    print(f"Infelizmente, você foi reprovado. Sua média foi {media:.1f} e sua frequência foi {frequencia:.1f}%")