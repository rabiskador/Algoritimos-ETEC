print("""
Exericio 3:
Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que diga se ela poderá ou não votar esté ano? 
(não é necessário considerar o mes em que a pessoa nasceu,considerar somente que a pessoa deve ter 16 anos para votar)
""")

ano_nasc = int(input("Digite seu ano de nascimento: "))
ano_atual = int(input("Digite seu ano atual: "))

idade = ano_atual - ano_nasc
pode_votar = idade >= 16

if pode_votar:
    print(f"Voce {idade} anos, você ja tem direito a votar, exerça sua cidadania com sabedoria 👍")

else:
    print(f"Voce tem {idade} anos, Infelizmente voce não possui idade para votar ")