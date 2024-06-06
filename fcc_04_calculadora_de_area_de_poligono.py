'''Calculadora de Área de Polígono'''


class Rectangle:
    '''Clase para crear instancias de rectangulo ulizando ancho y alto'''

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, new_value):
        '''Método para cambia el ancho del rectangulo'''
        self.width = new_value

    def set_height(self, new_value):
        '''Método para cambia el alto del rectangulo'''
        self.height = new_value

    def get_area(self):
        '''Método para calcular el area del rectangulo'''
        return self.width * self.height

    def get_perimeter(self):
        '''Método para calcular el perimetro del rectangulo'''
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        '''Método para calcular la diagonal del rectangulo'''
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        '''Método para dibujar el rectangulo utilizando asteriscos'''
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        if self.width <= 50 and self.height <= 50:
            picture = ''
            x = 0
            while x < self.height:
                picture += ''.center(self.width, "*") + '\n'
                x += 1
        return picture

    def get_amount_inside(self, another_shape):
        '''Método para calcular cuantas veces cabe otro rectangulo en el actual sin rotarlos'''
        return self.width // another_shape.width * self. height // another_shape.height


class Square(Rectangle):
    '''Subclase para crear instancias de cuadrado utilizando lado'''

    def __init__(self, side):
        super().__init__(self, side)
        self.width = side
        self.height = side

    def __str__(self):
        return f'Square(side={self.width})'

    def set_side(self, new_value):
        '''Método para cambia el lado del cuadrado'''
        self.width = new_value
        self.height = new_value

    def set_width(self, new_value):
        '''Método para cambia el lado del cuadrado utilizando el ancho'''
        self.set_side(new_value)

    def set_height(self, new_value):
        '''Método para cambia el lado del caudrado utilizando el alto'''
        self.set_side(new_value)


# ********** ********** ********** ********** ********** ********** ********** #
# Ejemplo de uso #

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))

# ********** ********** ********** ********** ********** ********** ********** #
