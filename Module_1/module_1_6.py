my_dict = {'Mike': 1997, 'Joe': 2000, 'John': 1995}
print(my_dict)
print('Existing value:', my_dict.get('Mike'))
print('Not existing value:', my_dict.get('Bob'))
my_dict.update({'Kris': 1992,
               'Ashley': 2003})
s = (my_dict.pop('Joe'))
print('Deleted value:',(s))
print('Modified dictionary:',my_dict)

my_set = {6,6,'s','v',7,'v'}
print('Set:',my_set)
my_set.add(10)
my_set.add('box')
my_set.remove('v')
print('Modified set:',my_set)


