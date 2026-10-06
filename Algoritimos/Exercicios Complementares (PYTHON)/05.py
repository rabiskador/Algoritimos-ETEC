print("""
Desafio 05 —Leia a idade de uma pessoa e verifique se ela possui ingresso.

Regras para entrada:
- Se a pessoa tiver 18 anos ou mais, poderá entrar somente se possuir ingresso.
- Se a pessoa tiver menos de 18 anos, deverá estar acompanhada de um responsável e possuir ingresso.
- Considere "sim" ou "s" como resposta positiva.

Ao final, informe:
- "Entrada liberada"
- "Entrada negada"
""")

idade = int(input("Digite sua idade: "))

ingresso = input("Possui ingresso? ").strip().lower()
ingresso_valido = ingresso == "sim" or ingresso == "s"

if idade >= 18:
    if ingresso_valido:
        print("Entrada liberada")
    else:
        print("Entrada negada")

else:
    responsavel = input("Está com o responsável? ").strip().lower()
    acompanhado = responsavel == "sim" or responsavel == "s"

    if ingresso_valido and acompanhado:
        print("Entrada liberada")
    else:
        print("Entrada negada")