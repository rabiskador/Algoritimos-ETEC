print("""
Exercicio 7:
Ler o salário e o valor das vendas efetuadas pelo vendedor de uma empresa. 
Sabendo-se que ele recebe uma comisão de 3% sobre sobre o total de vendas até R$ 1.500,00 mais 5% sobre 
o que ultrapassar esse valor, calcular e motrar o seu salario total`);
""")

salario = float(input("Insira seu salario: "));
valor_vendas = float(input("Insira o valor das suas vendas: "));

if valor_vendas <= 1500:
    comissao = (valor_vendas * 3) / 100 + salario
    print(f"Voce ira receber a porcentagem de 3% do valor vendido seu salario total vai para: R$ {comissao:.2f}")\

else:
    comissao = (valor_vendas * 5) / 100 + salario
    print(f"Voce ira receber a porcentagem maxima 5% do valor vendido seu salario total vai para: R$ {comissao:.2f}")