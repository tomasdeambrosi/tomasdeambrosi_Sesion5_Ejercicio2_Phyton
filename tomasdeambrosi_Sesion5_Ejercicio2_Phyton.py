def esNumeroPrimo(numero):
    if numero == 1 or numero == 0:
        return 'El número es ' + str(numero)
    for i in range (2, numero):
        if numero % i ==0:
            return 'El número '+ str(numero) + ' no es primo, es divisible por ' + str(i)
        else:
            continue

    for j in range (2, numero):
        if numero % i != 0:
            return 'El número ' + str(numero) + ' es primo'

num = input('Ingrese un número')

print(esNumeroPrimo(int(num)))