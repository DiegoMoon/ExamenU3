primNum = int(input("Ingrese un numero: "))
segunNum = int(input("Ingrese otro numero: "))

def numMaximo(primNum, segunNum): 
      
    if primNum >= segunNum: 
        return primNum
    else: 
        return segunNum

print(numMaximo(primNum, segunNum))

def mayorEdad(edad):
    if edad >= 18:
        print("Eres mayor de edad, acceso permitido")
        return "Eres mayor de edad"
    else:
        print("No cumples con la edad, no puedes acceder")
        return "No eres mayor de edad"

if  __name__== "main":
        numMaximo(23,43)
        mayorEdad(18)