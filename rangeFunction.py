for x in range(10):
    print(x)

for y in range(1,11):
    print(y)

#print all even number till 100 using range function
for num in range(0,100,2):
    print(num, end=" ")

print("---------------")

#print all odd number till 100 using range function
for num in range(0, 100):
    if num % 2 != 0:
        print(num, end=" ")

print("---------------")


#print table of 23 till 10 using range
n = 23
for i in range(11):
   print(n, 'x', i, '=', n*i)

print("---------------")

#print all even and odd using only range not condition statement
for num in range(1,100,2):
    print(num, end=" ")