'''
Se Define Super clase para figuras geométricas
'''
class FiguraGeometrica:
    def __init__(self, ancho: float= None, alto: float= None):
        self.ancho = ancho
        self.alto = alto

#Encapsulamiento y validaciones que sean mayores a 0
    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, valor):
        if valor <= 0:
            raise ValueError("El ancho debe ser mayor que 0")
        self._ancho = valor

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, valor):
        if valor <= 0:
            raise ValueError("El alto debe ser mayor que 0")
        self._alto = valor

#Calculo del area y perimetro

    def area(self):
        return self._ancho * self._alto

    def perimetro(self):
        pass

    def __str__(self):
        return f"FiguraGeometrica(ancho={self._ancho}, alto={self._alto})"


