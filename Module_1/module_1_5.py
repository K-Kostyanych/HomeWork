immutable_var = 3,7,'box', True
print(immutable_var)
immutable_var[0] = 5 #кортеж неизменяемый
print(immutable_var)

mutable_list = [3,5,7,8,9]
mutable_list[0] = 'a'
mutable_list[3] = 'c'
print(mutable_list)
