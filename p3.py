lista = []
numero = int(input("Cantidad de numeros que quieres ingresar(Positivos, Negativos): "))
negativo = 0
positivo = 0
 
 ## Pedira la cantidad de numeros que ingreso el usuario
for i in range(0, numero):
    while True:
        try:
            n = int(input("Escribe un número: "))
        except ValueError:
            print("Escribe un número.")
            continue
        break
    lista.append(n)
    if n<0:
        negativo = negativo + n
    else:
        positivo = positivo + n
 
 ## Mostrara la suma de numeros negativos y positivos
print("Suma números negativos es: ", negativo)
print("Suma números positivos es: ", positivo)