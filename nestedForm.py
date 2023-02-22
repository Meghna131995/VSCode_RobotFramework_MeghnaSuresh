list1=["Moolya", "Python", "classes", "learn"]
for x in list1:
    for y in x:
        print(y)


s="Meghna"
for z in s:
    print(z)

list2= [["a","b","c"],["d","e"]]
for t in list2:
    for q in t:
        print(q)

list4=[['india','delhi'],['usa','new jersy'],['canada','vancouver']]
#my country name is +country+ and i live in +city
for a in list4:
    print(a)
for b,c in list4:
        print("My country is " +b+ " and I live in " +c)


directory1 = dict(list4)
print(directory1)

for a,b in directory1.items():
    print(a,b)