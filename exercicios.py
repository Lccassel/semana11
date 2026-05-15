A = []
B = []

# Leitura de 10 valores distintos no vetor A
while len(A) < 10:
    numero = int(input(f"Digite o {len(A)+1}º valor: "))

    if numero not in A:
        A.append(numero)
    else:
        print("Valor repetido! Digite um número diferente.")

# Criando o vetor B com ordem inversa de A
B = A[::-1]

# Resultado
print("\nVetor A:", A)
print("Vetor B (ordem inversa):", B)