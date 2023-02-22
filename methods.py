# def print_char(string):
#     for c in string:
#         print(c)
# print_char("Python")

def add(a,b,c):
    return a+b+c
z=add(2,5,7)
print(z)

print("-------------")

#fibonacci series

a = 1
b = 0
print(b)
print(a)
for i in range(0,50):
    c = b
    b = a
    a = c + b
    print(a)