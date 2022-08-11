class alumn:
    def __init__(self,nom,ape,edad,email):
        self.nom = nom
        self.ape = ape
        self.edad = edad
        self.email = email

alumno1 = alumn
alumno1.nom = input("Ingrese su nombre: ")
alumno1.ape = input("Ingrese su apellido: ")
alumno1.edad = input("Ingrese su edad: ")
alumno1.email = input("Ingrese su email: ")
        
print(" Nombre:", alumno1.nom, "\n", "Apellido:", alumno1.ape, "\n", "edad:", alumno1.edad, "\n", "Email:", alumno1.email)