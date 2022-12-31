linha = input().split()
linha2 = input().split()


codigo1 = int(linha[0])
quantidade1 = int(linha[1])
valor1 = float(linha[2])

codigo2 = int(linha2[0])
quantidade2 = int(linha2[1])
valor2 = float(linha2[2])

print(f"VALOR A PAGAR: R$ {quantidade1 * valor1 + quantidade2 * valor2:.2f}")
