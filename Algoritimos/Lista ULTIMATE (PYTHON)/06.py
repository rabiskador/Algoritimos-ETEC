print("""
Exercicio 6:
A jornada de trabalho semanal de um funcionário é de 40 horas. Os funcionários que trabalhar mais de 40 horas receberá hora extra.
Cujo cálculo é o valor da hora regular com um acréscimo de 50% . 
Escreva um algoritmo que leia o número de horas trabalhadas em um mes
o salário por hora e mostre o salário total do funcionário, 
que deverá ser acrescido das horas extras, caso tenham sido trabalhadas(considere que mes possua 4 semanas exatas)
""")

valor_hora = float(input("Insira o valor que voce ganha por hora: "))
horas_trabalhadas = float(input("Insira suas horas trabalhadas: "))

salario_total = horas_trabalhadas * valor_hora

if horas_trabalhadas > 160:
    horas_extras = horas_trabalhadas - 160
    valor_hora_extra = (horas_extras * valor_hora) / 2
    salario_extra = salario_total + valor_hora_extra
    print(f"A sua quantidade de horas extras foi de {horas_extras} horas. O valor de horas extra é de R$ {valor_hora_extra:.2f}")
    print(f"O valor total a receber será de R$ {salario_extra:.2f}")

else:
    print(f"O valor a ser recebido é de R$ {salario_total:.2f}")