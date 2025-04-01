#Faça um algoritimo que leia n valor inteiros e escreva quantos valores são negativos

numeros_negativos = 0
n = int(input("Quantos valores voce irá digitar: "))

for i in range(n):
    valor = int(input("Digite os valores: "))
    if valor < 0:
        numeros_negativos += 1
print(numeros_negativos)

    