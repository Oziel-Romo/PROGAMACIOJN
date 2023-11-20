class TresProgramas:
    def __init__(self):
        self.compra = float(input("Ingrese el monto de su compra: "))

    def pagar(self):
        if self.compra < 500:
            return f"SU COMPRA NO TIENE DESCUENTO: {self.compra:.2f}"
            
        elif 500 <= self.compra <= 1000:
            descuento5 = self.compra * 0.05
            total_con_descuento = self.compra - descuento5
            return f"TIENE DESCUENTO DE 5%: {descuento5:.2f} \n SU TOTAL ES : {total_con_descuento:.2f}"
            
        elif 1000 < self.compra < 7000:
            descuento11 = self.compra * 0.11
            total_con_descuento = self.compra - descuento11
            return f"TIENE DESCUENTO DE 11%: {descuento11:.2f} \n SU TOTAL ES : {total_con_descuento:.2f}"
        
        elif 7000 <= self.compra < 15000:
            descuento18 = self.compra * 0.18
            total_con_descuento = self.compra - descuento18
            return f"TIENE DESCUENTO DE 18%: {descuento18:.2f} \n SU TOTAL ES : {total_con_descuento:.2f}"
        
        elif self.compra >= 15000:
            descuento25 = self.compra * 0.25
            total_con_descuento = self.compra - descuento25
            return f"TIENE DESCUENTO DE 25%: {descuento25:.2f} \n SU TOTAL ES : {total_con_descuento:.2f}"

    def archivos_texto(self):
        with open("resultados_tres_programas.txt", 'w') as archivo:
            archivo.write(self.pagar())

# Bloque principal
programas = TresProgramas()
programas.archivos_texto()


class Dinosaurio:
    def __init__(self):
        self.nombre = input("Ingrese su nombre: ")
        self.peso = float(input("Ingrese su peso: "))
        self.longitud = float(input("Ingrese su longitud: "))

    def convertir_medidas(self):
        self.peso *= 1000  # Convertir peso a kilogramos
        self.longitud *= 0.3047  # Convertir longitud a metros

    def archivos_texto(self):
        with open("resultados_dinosaurio.txt", 'w') as archivo:
            archivo.write(f"Nombre: {self.nombre}\nPeso en KG: {self.peso:.2f}\nLongitud en Metros: {self.longitud:.2f}")

# Bloque principal
dinosaurio1 = Dinosaurio()
dinosaurio1.convertir_medidas()
dinosaurio1.archivos_texto()


class Gasolinera:
    def __init__(self):
        self.galones = float(input("¿Cuántos galones desea comprar?"))

    def monto_pago(self):
        litros_por_galon = 3.785
        precio_por_litro = 8.20

        galones_convertidos_a_litros = self.galones * litros_por_galon
        total_pagar = galones_convertidos_a_litros * precio_por_litro

        return total_pagar

    def archivos_texto(self):
        with open("resultados_gasolinera.txt", 'w') as archivo:
            archivo.write(f"Galones: {self.galones:.2f}\nTotal a pagar: {self.monto_pago():.2f}")

# Bloque principal
gasolinera1 = Gasolinera()
gasolinera1.archivos_texto()
