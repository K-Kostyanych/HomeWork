def addition(num):
    return num + 1
s = 3
addition = addition(s)
print(addition)

def convert(minutes):
    seconds = minutes * 60
    return seconds
print(convert(minutes = 5))


def flatten_structure(data_structure):
    # Создаем новый список для хранения плоской структуры
    new_data = []

    # Проходим по всем элементам исходной структуры
    for element in data_structure:
        # Если элемент является списком, добавляем все его элементы в новый список
        if isinstance(element, list):
            new_data.extend(element)

        # Если элемент является словарем, добавляем все ключи этого словаря в новый список
        elif isinstance(element, dict):
            new_data.extend(element.keys())

        # Если элемент является кортежем, добавляем все элементы кортежа в новый список
        elif isinstance(element, tuple):
            new_data.extend(element)

        # Если элемент является строкой, добавляем его в новый список
        elif isinstance(element, str):
            new_data.append(element)

    return new_data


# Пример использования функции
data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]
flattened_data = flatten_structure(data_structure)
print(flattened_data)

