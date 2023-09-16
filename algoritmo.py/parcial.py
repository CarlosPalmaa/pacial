def calcular_superficie_rectangulo(base, altura):
    return base * altura

# Bloque principal del programa
lado1_rectangulo1 = float(input("Ingrese la longitud del primer lado del rectángulo 1: "))
lado2_rectangulo1 = float(input("Ingrese la longitud del segundo lado del rectángulo 1: "))

lado1_rectangulo2 = float(input("Ingrese la longitud del primer lado del rectángulo 2: "))
lado2_rectangulo2 = float(input("Ingrese la longitud del segundo lado del rectángulo 2: "))

superficie_rectangulo1 = calcular_superficie_rectangulo(lado1_rectangulo1, lado2_rectangulo1)
superficie_rectangulo2 = calcular_superficie_rectangulo(lado1_rectangulo2, lado2_rectangulo2)

print("Superficie del rectángulo 1:", superficie_rectangulo1)
print("Superficie del rectángulo 2:", superficie_rectangulo2)

if superficie_rectangulo1 > superficie_rectangulo2:
    print("El rectángulo 1 tiene una superficie mayor.")
elif superficie_rectangulo1 < superficie_rectangulo2:
    print("El rectángulo 2 tiene una superficie mayor.")
else:
    print("Ambos rectángulos tienen la misma superficie.")
