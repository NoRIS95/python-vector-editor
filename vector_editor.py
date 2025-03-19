from shapes import Point, Line, Circle, Square

class VectorEditor:
    def __init__(self):
        self.shapes = []

    def create_point(self, x, y):
        point = Point(x, y)
        self.shapes.append(point)

    def create_line(self, x1, y1, x2, y2):
        start = Point(x1, y1)
        end = Point(x2, y2)
        line = Line(start, end)
        self.shapes.append(line)

    def create_circle(self, x_center, y_center, radius):
        center = Point(x_center, y_center)
        circle = Circle(center, radius)
        self.shapes.append(circle)

    def create_square(self, x_point_left, y_point_left, length_side):
        top_left = Point(x_point_left, y_point_left)
        square = Square(top_left, length_side)
        self.shapes.append(square)

    def delete_shape(self, index):
        if len(self.shapes) == 0:
            return "Список пустой. Нечего удалять.\n"
        if 0 <= index < len(self.shapes):
            self.shapes.pop(index)
            return "Фигура успешно удалена\n"
        else:
            return f"Неправильно введён индекс! Это должно быть число от 0 до {len(self.shapes) - 1}\n"

    def list_shapes(self):
        if len(self.shapes) == 0:
            print("Список фигур пуст\n")
        for i, shape in enumerate(self.shapes):
            print(f'{i}: {shape}')
        print("")

    def run(self):
        while True:
            command = input("Введите команду (создать, удалить, отобразить, помощь или выход):\n").strip().lower()

            if command == "выход":
                print("До свидания!")
                break

            elif command == "создать":
                figure = input("Какую фигуру хотите создать (введите точка, отрезок, круг или квадрат)?\n").strip().lower()
                if figure == "точка":
                    try:
                        x, y = map(float, input("Введите x и y этой точки через пробел: ").split())
                        self.create_point(x, y)
                        print("Точка успешно создана\n")
                    except ValueError:
                        print("Ошибка при введении данных\n")
                elif figure == "отрезок":
                    try:
                        x1, y1 = map(float, input("Введите x и y первой точки через пробел: ").split())
                        x2, y2 = map(float, input("Введите x и y второй точки через пробел: ").split())
                        self.create_line(x1, y1, x2, y2)
                        print("Отрезок успешно создан\n")
                    except ValueError:
                        print("Ошибка при введении данных\n")
                elif figure == "круг":
                    try:
                        x, y = map(float, input("Введите x и y центра через пробел: ").split())
                        radius = float(input("Введите радиус круга: "))
                        self.create_circle(x, y, radius)
                        print("Круг успешно создан\n")
                    except ValueError:
                        print("Ошибка при введении данных\n") 
                elif figure == "квадрат":
                    try:
                        x, y = map(float, input("Введите x и y левой верхней точки квадрата через пробел: ").split())
                        side = float(input("Введите сторону квадрата: "))
                        self.create_square(x, y, side)
                        print("Квадрат успешно создан\n")
                    except ValueError:
                        print("Ошибка при введении данных\n")
                else: 
                    print("Такой фигуры не существует\n")
            
            elif command == "удалить":
                try:
                    index = int(input("Введите индекс фигуры в списке, которую хотите удалить: "))
                    del_shape = self.delete_shape(index)
                    print(del_shape)
                except ValueError:
                        print(f"Неправильно введён индекс. Это должно быть число от 0 до {self.shapes}")
            
            elif command == "отобразить":
                self.list_shapes()

            elif command == "помощь":
                print("Доступные команды:")
                print("  создать - создать новую фигуру")
                print("  удалить - удалить фигуру по индексу")
                print("  отобразить - показать список фигур")
                print("  выход - завершить программу\n")

            else:
                print("Такой команды нету\n")