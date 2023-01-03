linha = input().split()

a = float(linha[0])
b = float(linha[1])
c = float(linha[2])

print(f"TRIANGULO: {(a * c) / 2:.3f}")
print(f"CIRCULO: {c ** 2 * 3.14159:.3f}")
print(f"TRAPEZIO: {((a + b) * c) / 2:.3f}")
print(f"QUADRADO: {b ** 2:.3f}")
print(f"RETANGULO: {a * b:.3f}")
