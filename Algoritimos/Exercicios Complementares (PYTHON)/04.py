print("""
Desafio 04 — Crie um programa para uma biblioteca:

Leia a idade da pessoa;
Pergunte se ela possui cadastro, recebendo "sim" ou "nao";
A pessoa poderá pegar livros se tiver 18 anos ou mais e cadastro;
Caso contrário, não poderá pegar livros.
Use o operador and.
""")

idade = int(input("Digite sua idade: "))
cadastro = input("Você possui cadastro? (Responda com sim ou nao) ").strip().lower()

if idade >= 18 and cadastro == "sim":
    print("Livro liberado")

else:
    print("Livro negado")
