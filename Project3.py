#list
l1= [13,'Meghna', 1995, True]
print(l1[0])
print(l1[3])
#   0     1     2      3    4    5
l3=[10,'Meghna',10,'Meghna',10, 90]
print(l3)
print("Number of times Meghna is repeated:")
print(l3.count('Meghna'))

print(l3[0:5:4])
l3.remove('Meghna')
l3.remove('Meghna')
print(l3)

#---------------------------------------------

l2=[1,2,3,4,5,6,7,8,9]
print(l2[0:10:3])
l2.append('Suresh')
print(l2)
l2.insert(0,'Meghna')
print(l2)
#---------------------------------------------

l4=['Meghna','India','Sushant','Moolya']
l4.sort()
print(l4)

l5=[88,66,44,23,99,00,12]
l5.sort(reverse= True)
print(l5)

l5.pop()
print(l5)