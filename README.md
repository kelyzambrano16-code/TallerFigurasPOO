Taller Figuras Geométricas (POO en Python)

Este proyecto implementa clases de figuras geométricas aplicando los conceptos de:
- Encapsulamiento con `@property` y `@setter`.
- Herencia y polimorfismo.
- Sobrescritura de métodos (`__str__`, `area`, `perimetro`).
- Validaciones internas (valores mayores que 0).
- Estándar PEP8 para nombres y estructura.
  
Clases
- FiguraGeometrica  
  Clase base con atributos privados (`_ancho`, `_alto`), validaciones y métodos comunes.
- Cuadrado
  Hereda de FiguraGeometrica. Recibe un solo parámetro (`lado`) y sobrescribe `area`, `perimetro` y `__str__`.
- Rectangulo 
  Hereda de FiguraGeometrica. Recibe `ancho` y `alto`, sobrescribe `area`, `perimetro` y `__str__`.

Ejecución
Ejemplo de salida al ejecutar `main.py`:

<img width="1346" height="755" alt="Captura de pantalla 2025-11-19 182747" src="https://github.com/user-attachments/assets/31d8abba-4fe7-4278-9638-8b9f3277db9d" />
<img width="780" height="590" alt="image" src="https://github.com/user-attachments/assets/2eb82b40-65b8-41e1-bcbd-a73f2feb1cdc" />

