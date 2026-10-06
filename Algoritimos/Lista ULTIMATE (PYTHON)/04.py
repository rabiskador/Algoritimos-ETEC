print("""
Exercicio 4:
Ler dois valores (considere que não serão lidos valores iguais) e mostre o maior deles.`);
""")

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

maior1 = valor1 > valor2
maior2 = valor2 > valor1

if maior1: 
    print(f"O primeiro valor digitado é o mais alto = {valor1}")

elif maior2:
    print(f"O segundo valor digitado é o mais alto = {valor2}")

else:
    print(f"Valores iguais não é permitido")