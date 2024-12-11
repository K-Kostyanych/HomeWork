#обьеденение одинак элем списка в один список
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
result1 = [elem for elem in a if elem in b]
print (result1)

result2 = list(set(a) & set(b))
print(result2)

#cортировка элементов словаря по возрастанию
my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
sorted_ascending = sorted(my_dict.items(), key=lambda x: x[1])
print("Сортировка по возрастанию:")
for key, value in sorted_ascending:
    print(f"{key}: {value}")

#слияние неск словарей в один
my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
my_dict2 = {'v': 370, 'k': 999, 'n': 777, 's': 10000, 'm': 666 }
result = {**my_dict, **my_dict2}
print(result)





