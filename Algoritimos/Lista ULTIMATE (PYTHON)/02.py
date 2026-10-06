print("""
Exercicio 2:
Ler as notas da primeira e segunda avaliação de um aluno e calcular a média simples e escrever uma mensagem que diga se 
aluno foi ou não aprovado (considerar que se a nota for >= 6 o aluno será aprovado) Escrever a média calculada.
""")

nota1 = float(input("Insira sua primeira nota: "))
nota2 = float(input("Insira sua segunda nota: "))

media = (nota1 + nota2) / 2
aprovado = media >= 6

if aprovado:
    print(f"Aprovado, segue a sua media {media:.1f}")

else:
    print(f"Reprovado, segue a sua media {media:.1f}")