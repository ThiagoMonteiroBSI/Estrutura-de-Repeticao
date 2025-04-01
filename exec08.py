#Faça um algoritmo que leia a quantidade de tinta que uma caneta, e enquanto a caneta tiver tinta para escrever, escreva “Enquanto tem tinta a caneta escreve...”. Considere que a cada comando de escrita a caneta gasta 2% da tinta que possui.

tinta = float(input("Digite a porcentagem de tinta: "))

if tinta <= 0 or tinta >= 100:
    print("A caneta tem tinda ainda :)")
else:
    while tinta > 0:
        print("Enquanto tem tinta a caneta escreve..")
        tinta -= 2
    print("Acabou-se")
