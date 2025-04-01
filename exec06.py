soma = 0
quantidade = 2

for i in range(quantidade):
    altura = int(input("Digite sua altura (em cm): "))

    soma +=altura

    media = soma/quantidade
print(f"A média ponderada das alturas é: {media}")
