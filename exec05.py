#faça um algoritimo que calcule e escreva a soma dos números pares e a soma dos números ímpares entre 1 e 100

soma_pares = 0
soma_impares = 0

for numero in range(1, 101):
    if numero % 2 == 0:
        soma_pares += numero
    else:
        soma_impares += numero

print(f"Soma dos Pares: {soma_pares}")
print(f"Soma dos Impares: {soma_impares}")
    