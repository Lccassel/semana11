vetor = []

# Leitura de 10 valores distintos
while len(vetor) < 10:
    numero = int(input(f"Digite o {len(vetor)+1}º valor: "))

    if numero not in vetor:
        vetor.append(numero)
    else:
        print("Valor repetido! Digite um número diferente.")

# Verificando valores maiores que 100
maiores_100 = []

for numero in vetor:
    if numero > 100:
        maiores_100.append(numero)

# Resultados
print("\nValores digitados:", vetor)
print("Quantidade de valores maiores que 100:", len(maiores_100))
print("Valores maiores que 100:", maiores_100)
