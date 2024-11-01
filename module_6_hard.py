import math
class Figure:
    sides_count = 0
    def __init__(self, color, *sides):
        self.__sides = sides #список сторон (целые числа)
        self.__color = color #список цветов в формате RGB
        self.filled = False #закрашенный, bool

    def get_color(self): #возвращает список RGB цветов.
        return self.__color

    def __is_valid_color(self, r, g, b ): #Проверяет корректность переданных значений RGB
        return all(isinstance(i, int) and 0 <= i <= 255 for i in (r, g, b))

    def set_color(self,r, g, b): #Устанавливает новый цвет для фигуры
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            print("Некорректный формат цвета")

    def __is_valid_sides(self, sides):
        #Проверка, что все стороны - целые положительные числа, и их количество равно sides_count
        return all(isinstance(j, int) and j > 0 for j in sides) and len(sides) == self.sides_count

    def get_sides(self):
        return self.__sides

    def __len__(self): #Возвращает периметр фигуры
        return sum(self.__sides)

    def set_sides(self, *new_sides): #Изменяет стороны фигуры, если количество новых сторон совпадает с sides_count
        if self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides)  # Устанавливаем новый список сторон
        else:
            print('Некорректное количество сторон, стороны остаются неизменными')


class Circle(Figure):
    sides_count = 1 #Круг имеет одну сторону (окружность)
    def __init__(self, color, circumference):
        super().__init__(color, circumference)
        self.__radius = circumference / (2 * math.pi)  # Рассчитываем радиус из длины окружности

    def get_square(self): #Возвращает площадь круга
        return math.pi * self.__radius ** 2

class Triangle(Figure):
    sides_count = 3  # У треугольника 3 стороны

    def get_square(self):  # Формула Герона для расчёта площади треугольника
        a, b, c = self.get_sides()  # Получаем стороны треугольника
        p = (a + b + c) / 2  # Полупериметр
        return math.sqrt(p * (p - a) * (p - b) * (p - c))  # Площадь по формуле Герона для треугольника

class Cube(Figure):  # class Куб
    sides_count = 12  # # У куба 12 рёбер

    def __init__(self, color, edge_length):
        super().__init__(color, *([edge_length]) * 12)  # Создаём куб с 12 одинаковыми рёбрами

    def get_volume(self):
        # Возвращаем объём куба
        edge_length = self.get_sides()[0]  # Все рёбра одинаковы
        return edge_length ** 3  # Объём куба

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())














