class TresProgramas:
    def __init__(self):
        self.compra = float(input("Ingrese el monto de su compra: "))

    def pagar(self):
        if self.compra < 500:
            print(f"SU COMPRA NO TIENE DESCUENTO: {self.compra:.2f}")
            
        elif 500 <= self.compra <= 1000:
            descuento5 = self.compra * 0.05
            total_con_descuento = self.compra - descuento5
            print(f"TIENE DESCUENTO DE 5%: {descuento5:.2f} \n SU TOTAL ES : {total_con_descuento:.2f}")
            
        elif 1000 < self.compra < 7000:
            descuento11 = self.compra * 0.11
            total_con_descuento = self.compra - descuento11
            print(f"TIENE DESCUENTO DE 11%: {descuento11:.2f} \n SU TOTAL ES : {total_con_descuento:.2f}")
        
        elif 7000 <= self.compra < 15000:
            descuento18 = self.compra * 0.18
            total_con_descuento = self.compra - descuento18
            print(f"TIENE DESCUENTO DE 18%: {descuento18:.2f} \n SU TOTAL ES : {total_con_descuento:.2f}")
        
        elif self.compra >= 15000:
            descuento25 = self.compra * 0.25
            total_con_descuento = self.compra - descuento25
            print(f"TIENE DESCUENTO DE 25%: {descuento25:.2f} \n SU TOTAL ES : {total_con_descuento:.2f}")

# Bloque principal
programas = TresProgramas()
programas.pagar()
