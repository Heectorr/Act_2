import re
un = 0
i = 0
lista = []
 
 
class veh(): ##Clase de datos de Vehiculo
    def __init__(self, unidad, marca, modelo, km, recorrido):
        self.unidad = unidad
        self.marca = marca
        self.modelo = modelo
        self.km = km
        self.recorrido = recorrido

def recorrido(n):
    veh.km = veh.km + n
    return n 

 ## Pedira el numero de unidades que se daran de alta
while True:
    try:
        veh.unidad = int(input("Numero de unidades que se daran de alta: "))
        if veh.unidad > 0 :
            break
        print("Ingresa un numero válido")
    except ValueError:
        print("Debes escribir un número.")
 
unidad = veh.unidad
 
for i in range(0, unidad):
    ## Numero unidades
    uni = ""
    while not re.match("^\S{2}(-)\d{3}$", uni):
        uni = input("Número de unidad: ")

    ## Valida los km recorridos
    while True:
        try:
            veh.km = int(input("Numero de km que tiene la unidad? "))
            if veh.km > 0 :
                lista.append(veh.km)
                break
            print("Ingresa un número positivo.")
        except ValueError:
            print("Escribe un número.")
        n = veh.km

         ##Valida la marca del vehículo
    while True:
        veh.marca = str(input("Marca del vehículo: "))
        if veh.marca.isalpha():
            break       
    lista.append(veh.marca)

     ##Valida el modelo/año del vehículo
    while True:
        veh.modelo = str(input("Modelo/Año que es el vehículo: "))
        if veh.modelo.isdigit():
            if veh.modelo >= "2018" or veh.modelo <= "2021":
                break    
    lista.append(veh.modelo)