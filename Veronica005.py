from random import shuffle

a = [1,2,3,4,5,6,7]
print(a)
shuffle(a)
print(a)

print(max(a), min(a))

b = ['A', '7', '3', 'i', 'J', 'z', '#']
print(max(b), min(b))

print('82h32U79da'.find('2U7'))

print('82h32U79da'.find('I9'))

print('82h32U79da'.__contains__('2U'))

print('82h32U79da'.__contains__('26U'))

lst = [x**2 for x in range(0,11)]
print('lst', lst)