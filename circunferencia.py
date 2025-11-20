"""Clase Circunferencia que hereda de FiguraGeometrica."""

from figura_geometrica import FiguraGeometrica
import math

class Circunferencia(FiguraGeometrica):

    def __init__(self, radio: float):
        FiguraGeometrica.__init__(self,radio, radio)  # usamos ancho=alto=radio

    def area(self) -> float:
        return math.pi * (self.ancho ** 2)

    def perimetro(self) -> float:
        return 2 * math.pi * self.ancho

    def __str__(self) -> str:
        return f"Circunferencia [radio={self.ancho}]"