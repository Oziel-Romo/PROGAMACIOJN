class Gasolinera:
    def __init__(self):
        self.galones = float(input("¿Cuántos galones desea comprar?"))

    def monto_pago(self):
        litros_por_galon = 3.785
        precio_por_litro = 8.20

        galones_convertidos_a_litros = self.galones * litros_por_galon
        total_pagar = galones_convertidos_a_litros * precio_por_litro

        return total_pagar

# Bloque principal
gasolinera1 = Gasolinera()
total = gasolinera1.monto_pago()
print(f"El total a pagar es: ${total:.2f}")
