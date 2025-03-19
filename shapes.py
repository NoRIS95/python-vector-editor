class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Точка({self.x}, {self.y})"

class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return f"Отрезок ({self.start}, {self.end})"

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
    
    def __str__(self):
        return f"Круг ({self.center}, Радиус = {self.radius})"

class Square:
    def __init__(self, point_left, length_side):
        self.point_left = point_left
        self.length_side = length_side

    def __str__(self):
        return f"Квадрат ({self.point_left}, Длина стороны: {self.length_side})"