my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
new_list = my_list[index]

while new_list >= 0 and index < len(my_list):
    new_list = my_list[index]
    index +=1
    if new_list < 0:
        break
    elif new_list == 0:
        continue
    print(new_list)

index += 1

