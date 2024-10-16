class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def __init__(self, owner:str,_model: str, _engine_power: int, color: str):
        self.owner = owner
        self._model = _model
        self._engine_power = _engine_power
        self.color = color
    def get_model(self):
        return f'Модель: {self._model}'
    def horse_power(self):
        return f'Мощность двигателя: {self._engine_power}'
    def get_color(self):
        return f'Цвет: {self.color}'

    def print_info(self):
        print(self.get_model())
        print(self.horse_power())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color: str):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    _PASSENGERS_LIMIT = 5

#Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
