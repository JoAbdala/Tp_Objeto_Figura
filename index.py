class Figura:
    
    def __init__(self, nombre) :
        self.nombre = nombre
    def perimetro(self):
        pass
    
    def area(self):
       pass
    def mostrarFigura(self):
        print("El nombre de la figura es:--> {}".format(self.nombre))

class Cuadrado(Figura):
    def __init__(self, lado):
        super().__init__("_>Cuadrado<_")
        self.lado = lado

    def perimetro(self):
        perimetro = 4 * self.lado
        print("El perímetro del cuadrado es:", perimetro)
        return perimetro

    def area(self):
        area = self.lado * self.lado
        print("El área del cuadrado es:", area)
        return area
    
    def __del__(self):
        print("El cuadrado  ha sido borrado.")
        
  
class Rectangulo(Figura):
    def __init__(self,  base, altura):
        super().__init__("_>Rectangulo<_")
        self.base = base
        self.altura = altura

    def perimetro(self):
        perimetro = (self.base + self.altura) * 2
        print("El perímetro del rectángulo es:", perimetro)
        return perimetro

    def area(self):
        area = self.base * self.altura
        print("El área del rectángulo es:", area)
        return area
    
    def __del__(self):
        print("El rectángulo ha sido borrado.")
    
class Triangulo(Figura):
    def __init__(self, lado1, lado2, lado3,altura):
        super().__init__("_>Trinagulo<_")
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.altura = altura
    def perimetro(self):
        perimetro = self.lado1 + self.lado2 + self.lado3
        print("El perimetro del trinagulo es: ",perimetro)
        return perimetro
    
    def area(self,altura):
        area = (self.lado1 * self.altura)/2
        print("El area del triangulo es: ",area)
        return area
    def __del__(self):
        print("El triangulo ha sido borrado. ")
    
    
cuadrado= Cuadrado (5)
rectangulo = Rectangulo(4, 6)
triangulo = Triangulo (6,6,6,5)



cuadrado.mostrarFigura()
cuadrado.perimetro()
cuadrado.area()

rectangulo.mostrarFigura()
rectangulo.perimetro()
rectangulo.area()

triangulo.mostrarFigura()
triangulo.perimetro()
triangulo.area(5)
