import math


class Figure:

    def __init__(self, color, *lengths):

        self.__sides = []
        if len(color) == 3:
            self.set_color(*color)
        else:
            self.__color = 0, 0, 0
        self.filled = False

        if len(lengths) == self.sides_count:
            self.set_sides(*lengths)
        else:
            self.set_sides(*[1] * self.sides_count)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if r < 0 or r > 255 or g < 0 or g > 255 or b < 0 or b > 255:
            return False
        else:
            return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        return self

    def __is_valid_sides(self, *args):
        if len(args) == self.sides_count and all(number > 0 and isinstance(number, int) for number in self.__sides):
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)


class Circle(Figure):

    def __init__(self, color, *lengths):
        self.sides_count = 1
        super().__init__(color, *lengths)
        self.__radius = None

    def get_square(self):
        self.__radius = len(self.get_sides()) / (2 * math.pi)
        return self.__radius ** 2 * math.pi


class Triangle(Figure):
    def __init__(self, color, *lengths):
        self.sides_count = 3
        super().__init__(color, *lengths)

    def get_square(self):
        s = len(self) / 2
        sides = self.get_sides()
        a = sides[0]
        b = sides[1]
        c = sides[2]
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area


class Cube(Figure):
    def __init__(self, color, *lengths):
        self.sides_count = 12

        if len(lengths) == 1:
            lengths = [lengths[0]] * self.sides_count

        else:
            lengths = [1] * self.sides_count

        super().__init__(color, *lengths)

    def get_volume(self):
        return self.get_sides()[0] ** 3


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
