print("""
Exercicio 2:
Leia três valores inteiros que representam os lados de um triângulo. O algoritmo deve verificar e informar se o triângulo é:
- Equilátero → os três lados são iguais.
- Isósceles → dois lados são iguais.
- Escaleno → os três lados são diferentes.
""")


valor_esquerdo_triangulo = int(input("Coloque o valor do lado esquerdo do triângulo: "))
valor_direito_triangulo = int(input("Coloque o valor do lado direito do triângulo: "))
valor_base_triangulo = int(input("Coloque o valor da parte de baixo do triângulo: "))


if valor_base_triangulo == valor_direito_triangulo == valor_esquerdo_triangulo:
    print("Seu triângulo é Equilátero. Os três lados são iguais")

elif (valor_base_triangulo != valor_direito_triangulo and
      valor_esquerdo_triangulo != valor_base_triangulo and
      valor_direito_triangulo != valor_esquerdo_triangulo):

    print("Seu triângulo é Escaleno. Os três lados são diferentes")

else:
    print("Seu triângulo é Isósceles. Dois lados são iguais")