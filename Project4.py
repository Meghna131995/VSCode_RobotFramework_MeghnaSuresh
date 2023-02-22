#set
#set is unordered, does not accept repetitive values

s={10,20,30,40,50,50,60,'K'}
print(s)
print(len(s))
s.add('Meghna')
print(s)
s.pop()
print(s)

#-------------------

a={1,2,3,4,5}
b={6,7,8,9,6}
z=a.union(b)
print(z)

z1=a.symmetric_difference(b)
print(z1)

c={6,7}
print(c.issubset((b)))