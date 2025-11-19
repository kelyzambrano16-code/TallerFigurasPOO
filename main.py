"""
Archivo principal del taller de POO.
Se crean objetos de Cuadrado y Rectángulo,
se muestran sus áreas y perímetros,
y se prueban validaciones de encapsulamiento.
"""

from cuadrado import Cuadrado
from rectangulo import Rectangulo


def sumar_areas(figuras: list) -> float:
    """Suma las áreas de una lista de figuras geométricas."""
    return sum(fig.area() for fig in figuras)


def sumar_perimetros(figuras: list) -> float:
    """Suma los perímetros de una lista de figuras geométricas."""
    return sum(fig.perimetro() for fig in figuras)


if __name__ == "__main__":
    # Creación de objetos válidos
    c1 = Cuadrado(5)
    c2 = Cuadrado(10)
    r1 = Rectangulo(4, 6)
    r2 = Rectangulo(3, 8)

    figuras = [c1, c2, r1, r2]

    # Mostrar resultados de cada figura
    for figura in figuras:
        print(f"{figura} -> Área: {figura.area()}, Perímetro: {figura.perimetro()}")

    # Demostración de encapsulamiento (error esperado)
    try:
        c_invalido = Cuadrado(-2)
    except ValueError as error:
        print("Error al crear cuadrado:", error)

    # Modificación de valores usando setters
    c1.ancho = 7
    c1.alto = 7
    print("Cuadrado modificado:", c1,
          "Área:", c1.area(),
          "Perímetro:", c1.perimetro())

    # Sumar áreas y perímetros
    print("Suma de áreas:", sumar_areas(figuras))
    print("Suma de perímetros:", sumar_perimetros(figuras))
