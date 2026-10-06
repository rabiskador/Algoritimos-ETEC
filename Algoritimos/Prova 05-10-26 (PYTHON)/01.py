print("""
Exercicio 1:
Leia a base e a altura de dois retângulos. Calcule e exiba a área de cada retângulo (base*altura) e informe:
- "Retângulo 1 possui maior área"
- "Retângulo 2 possui maior área"
- "Os dois possuem a mesma área"
""")

retangulo_1_altura = float(input("Coloque a altura do seu retângulo 1: "))
retangulo_1_base = float(input("Coloque a base do seu retângulo 1: "))

retangulo_2_altura = float(input("Coloque a altura do seu retângulo 2: "))
retangulo_2_base = float(input("Coloque a base do seu retângulo 2: "))


retangulo1_area = retangulo_1_base * retangulo_1_altura
retangulo2_area = retangulo_2_base * retangulo_2_altura


if retangulo1_area > retangulo2_area:
    print("Retângulo 1 possui maior área")

elif retangulo2_area > retangulo1_area:
    print("Retângulo 2 possui maior área")

else:
    print("Os dois possuem a mesma área")