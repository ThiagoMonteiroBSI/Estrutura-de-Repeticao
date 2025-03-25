#faça um algoritimo que leia 20 numeros inteiros e escreva, para cada um, se ele é par ou impar

number = 0

while number != 10:
    number = int(input("Write a number: "))
    if (number % 2) == 0:
        print("This number is pair")
    if (number % 2 ) != 0:
        print("This number is odd")