lis = []
p = 0

 ## Pedira 10 numero enteros
for i in range(1, 10+1):
    while True:
        try:
            n = int(input("Dame un número entero: "))
        except ValueError:
            print("Escribe un número.")
            continue
        break
    if n % 2 == 0:
        p = p + 1
    lis.append(n)
 

##Mostrara el numero de numeros pares, el numero minimo y maximo
print("El número de números pares es ", p)
print("La número minimo es ", min(lis))
print("La número máximo es ", max(lis))