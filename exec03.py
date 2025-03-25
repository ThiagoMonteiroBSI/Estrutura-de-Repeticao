amount_paires = 0
first_number = True
minor = 0
bigger = 0

while True:
    number = int(input(" Writes a int numer: "))
    if number == 0:
        break

    if first_number:
        minor = number
        bigger = number
        first_number = False
    else:
        if number < bigger:
            minor = number
        if number > bigger:
            bigger = number

    if first_number % 2 == 0:
        amount_paires +=1

    if not first_number:
        print(f" Quantidades de valores pares: {amount_paires}")
        print(f"Menor valor: {minor}")
        print(f"Maior valor: {bigger}")
