a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))

# Verifica se formam um triângulo
if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        print("Triângulo Equilátero")
    elif a == b or a == c or b == c:
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")
else:
    print("Os valores não podem formar um triângulo.")
