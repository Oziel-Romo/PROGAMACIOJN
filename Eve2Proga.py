class Operaciones:

    def __init__(self):
        self.valor1=int(input("Ingrese primer valor:"))
        self.valor2=int(input("Ingrese segundo valor:"))

    def sumar(self):
        su=self.valor1+self.valor2
        print("La suma es",su)

    def restar(self):
        re=self.valor1-self.valor2
        print("La resta es",re)

    def multiplicar(self):
        pro=self.valor1*self.valor2
        print("El producto es",pro)

    def division(self):
        divi=self.valor1/self.valor2
        print("La division es",divi)

# bloque principal
operacion1=Operaciones()
operacion1.sumar()
operacion1.restar()
operacion1.multiplicar()
operacion1.division()



class Cuadrado:

    def __init__(self,lado):
        self.lado=lado

    def mostrar_perimetro(self):
        per=self.lado*4
        print("El perimetro del cuadrado es:",per)

    def mostrar_superficie(self):
        sup=self.lado*self.lado
        print("La superficie del cuadrado es:",sup)

# bloque principal
cuadrado1=Cuadrado(12)
cuadrado1.mostrar_perimetro()
cuadrado1.mostrar_superficie()





class mayor_edad:
    def __init__(self):
        self.val1=int(input("ingrese su edad:"))
        
    def resultado(self):
        if self.val1 >= 18:
            print(" Eres mayor de edad puedes pasar")
        else:
            print("Acceso denegado,Eres menor de edad") 

#Bloque principal
prueba=mayor_edad()
prueba.resultado()




class Triangulo:

    def inicializar(self):
        self.lado1=int(input("Ingrese primer lado:"))
        self.lado2=int(input("Ingrese segundo lado:"))
        self.lado3=int(input("Ingrese tercer lado:"))

    def imprimir(self):
        print("Valores de los lados del triangulo")
        print("Lado 1",self.lado1)
        print("Lado 2",self.lado2)
        print("Lado 3",self.lado3)

    def lado_mayor(self):
        print("Lado mayor")
        if self.lado1>self.lado2 and self.lado1>self.lado3:
            print(self.lado1)
        else:
            if self.lado2>self.lado3:
                print(self.lado2)
            else:
                print(self.lado3)

    def es_equilatero(self):
        if self.lado1==self.lado2 and self.lado1==self.lado3:
            print("El triangulo es equilatero")
        else:
            print("El triangulo no es equilatero")

# bloque principal
triangulo1=Triangulo()
triangulo1.inicializar()
triangulo1.imprimir()
triangulo1.lado_mayor()
triangulo1.es_equilatero()