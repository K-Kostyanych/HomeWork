class House:
    houses_history = []
    def __new__(cls, *args):#название объекта добавляется в список
        house_name = args[0]
        cls.houses_history.append(house_name)
        return object.__new__(cls)

    def __init__(self, *args):#устанавливаются атрибуты
        self.name = args[0]
        self.number_of_floors = args[1]

    def __del__(self, *args):#выводится сообщение о сносе здания
        print(f'{self.name}, снесён, но он останется в истории')



h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

del h2
del h3

print(House.houses_history)


