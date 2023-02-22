import math
from multipledispatch import dispatch
@dispatch(int)
def sum(a):
    print("Square root value: ")
    print(a**2)
@dispatch(int,int,int,int)
def sum(a,b,c,d):
    print("Addition of 4 numbers: ")
    print(a+b+c+d)
@dispatch(int,int,int)
def sum(a,b,c):
    print("Multiplication of 3 values: ")
    print(a*b*c)
@dispatch(int,int)
def sum(p,q):
    t=p*q
    print("root value")
    print(t)
    if t<0:
        print("Not possible")
    else:
        r=math.isqrt(t)
        print("root of")
        print(r)
        if r**2==t:
            print("This is perfect square")
        else:
            print("This is not a perfect square")
sum(7)
sum(4,3,9,0)
sum(2,6,3)
sum(3,3)





