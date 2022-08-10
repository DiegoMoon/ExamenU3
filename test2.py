lugar = str(input("Ingresa tu lugar de nacimiento: "))
edad = int (input("Ingresa tu edad:  "))

if(edad >= 18):
    print(f'La persona con {edad} años puede votar en {lugar}')
else:
    print("Esta persona no tiene edad para votar")
