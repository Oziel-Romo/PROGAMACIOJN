class Dinosaurio:
    def __init__(self):
        self.nombre = input("Ingrese su nombre: ")
        self.peso = float(input("Ingrese su peso: "))
        self.longitud = float(input("Ingrese su longitud: "))


    def convertir_medidas(self):
        self.peso *= 1000  # Convertir peso a kilogramos
        self.longitud *= 0.3047  # Convertir longitud a metros
        print("PESO EN KG : ", self.peso)
        print("LONGITUD EN METROS :", self.longitud)


# Bloque principal
dinosaurio1 = Dinosaurio()
print("_________________________________________")
dinosaurio1.convertir_medidas()

