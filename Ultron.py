a = 7
a = a + a
print(a)

s = 'Hello World'
print(s, s[0], s[3])

x, y = 'some', 'more'
print("I'm going to inject %s text here, and %s text here."%(x,y))

my_list = ['one','two','three',4,5]
print(my_list[1], my_list[3])

my_dict = {'key1':'value1','key2':'value2'}
print(my_dict['key1'], my_dict['key2'])

t = ('one', 2, 'III', 2)
print(t[0],t[1],t[-1],t[-2])
print('index of turple', t.index(2), t.count(2))

list1 = [1,1,2,2,3,4,5,6,1,1]
listC = [1,2,[3,4,'hello']]
list2 = list1[2:]
list3 = list1[:5]
s1 = set(list1)
print(s1)

print('list2: ', list2)
print('list3: ', list3)
print('listC: ', listC)

bl1 = True; objN = None
print(bl1, 1>2)
print(objN)
objN = 3
print(objN)