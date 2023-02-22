from multipledispatch import dispatch
@dispatch(int,int)
def sum(a,b):
    print(a+b)
@dispatch (int,int,int)
def sum (a,b,c):
    print(a+b+c)
sum(10, 5)
sum(5, 10, 15)