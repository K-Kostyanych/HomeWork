#Задание 1
list_ = ('Python - это питон!')# вывести кол-во букв
for i in range(len(list_)):
    print(i)
print()
s = 0
for j in list_:
    s += 1
    print(s)
print()

def func_outer():
    x=2
    print('х равно', x)
    def func_inner():
       x=3

       func_inner()
    print('Локальное х сменилось на', x)
func_outer()
print()
#Задание 2
my_string = input('Здаров:')#вывести если ответ не пустой -True
if len(my_string) > 0:
    print(True)
else:
    print(False)
print()
#Задание 3
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]# вывести числа меньше 5
for i in a:
    if i < 5:
        print(i)
        print()
print(list(filter(lambda elem: elem < 5, a)))
print([elem for elem in a if elem < 5])
print()
#Задание 4
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
result1 = [elem for elem in a if elem in b]
result2 = list(set(a) & set(b))
print(result1)
print(result2)




















