print("""
Exercicio 5:
Ler dois valores (Considere que não serão lidos valores iguais) e mostre-os em ordem`);
""")

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

if valor1 > valor2:
    print(f"Os valores em ordem decrescente são: {valor1}, {valor2}")

elif valor2 > valor1:
    print(f"Os valores em ordem decrescente são: {valor2}, {valor1}")

else:
    print("Valores iguais não são permitidos")