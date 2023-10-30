list1 = [1,2,3,4,5,6,7,8,9,10]

for num in list1:
    if num % 3 == 1:
        print('3+1', num)
    elif num % 7 == 1:
        print('7+1', num)
    else:
        print('number ', num)


x = 0
while x < 10:
    print('x is currently: ',x)
    print(' x is still less than 10, adding 1 to x')
    x+=1
    if x==3:
        print('x==3')
    else:
        print('continuing...')
        continue