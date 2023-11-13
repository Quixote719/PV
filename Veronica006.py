n = [3,1,5,6,2,9,7]
l = ['e','a','c','g']
l.append('q')

print(n.pop())
n.extend(l)

print('n', n)

n2 = n.copy()
print(n2)

n2.insert(2,'k')
print(n2)

n2.remove('c')
n2.remove('e')
print(n2)

n2.reverse()
print(n, n2)