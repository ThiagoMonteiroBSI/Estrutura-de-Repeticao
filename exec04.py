#faça um algoritimo que calcule e escreva a soma dos números pares e a soma dos números ímpares entre 1 e 100

soma = 0 
soma_impar = 0 
cont = 0 

while cont < 100:
    cont = cont + 1
    if cont % 2  == 0:
     soma = soma + cont
else:
    soma_impar = soma_impar + cont 
    print(soma, soma_impar)