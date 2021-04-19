lista = []
lista_2= []

## Pedira 6 numeros
for i in range(1, 5+1):
    while True:
        try:
            n = int(input("Dame un número: "))
        except ValueError:
            print("Escribe un número.")
            continue
        break
    lista.append(n)
    lista_2.append(n*2)
 
## Mostrara el resultado de los numeros
print("Resultados de los numeros: ", lista_2[0:5])