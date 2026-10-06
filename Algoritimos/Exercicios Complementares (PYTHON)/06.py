print("""
Desafio 06 — Sistema de acesso para estudantes

Leia se a pessoa é estudante e se possui cadastro.

Regras:
- Se a pessoa for estudante e tiver cadastro, poderá acessar.
- Se a pessoa tiver cadastro, mas não for estudante, deverá estar acompanhada de um estudante.
- Caso contrário, o acesso será negado.
""")

estudante = input("Você é estudante? ").strip().lower()
eh_estudante = estudante == "sim" or estudante == "s"

cadastro = input("Você possui cadastro? ").strip().lower()
tem_cadastro = cadastro == "sim" or cadastro == "s"

if tem_cadastro and eh_estudante:
    print("Acesso liberado")

elif tem_cadastro:
    acompanhado = input("Você está acompanhado de um estudante? ").strip().lower()

    esta_acompanhada = acompanhado == "sim" or acompanhado == "s"

    if esta_acompanhada:
        print("Acesso liberado")
    else:
        print("Acesso negado")

else:
    print("Acesso negado")
