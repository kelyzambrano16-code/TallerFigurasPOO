from cuadrado import Cuadrado
from rectangulo import Rectangulo
from circunferencia import Circunferencia

def sumar_areas(figuras: list) -> float:
    return sum([fig.area() for fig in figuras])

def sumar_perimetros(figuras: list) -> float:
    return sum([fig.perimetro() for fig in figuras])

if __name__ == "__main__":
    # Crear objetos válidos
    c1 = Cuadrado(5)
    c2 = Cuadrado(3)
    r1 = Rectangulo(4, 6)
    r2 = Rectangulo(2, 8)
    circ = Circunferencia(7)

    figuras = [c1, c2, r1, r2, circ]

    # Mostrar resultados
    for f in figuras:
        print(f"{f} → Área: {f.area():.2f}, Perímetro: {f.perimetro():.2f}")

    # Demostración de validaciones (valor inválido)
    try:
        c_invalido = Cuadrado(-2)
    except ValueError as e:
        print("Error al crear cuadrado:", e)

    # Sumar áreas y perímetros
    print("Suma de áreas:", sumar_areas(figuras))
    print("Suma de perímetros:", sumar_perimetros(figuras))