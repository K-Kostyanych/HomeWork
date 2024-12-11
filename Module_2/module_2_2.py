first = 123
second = 456
third = 789
if first == second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
elif first != second != third and second !=first !=third and third != first != second:
    print(0)
else:
    print('None')
fourth = 42
fifth = 69
sixth = 42
if fourth == fifth == sixth:
    print(3)
elif fourth == fifth or fifth == sixth or fourth == sixth:
    print(2)
elif fourth != fifth != sixth and fifth != sixth != fourth and sixth != fourth != fifth:
    print(0)
else:
    print('None')






