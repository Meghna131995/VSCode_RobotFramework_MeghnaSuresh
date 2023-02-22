#if loops
marks=70
if marks>=90:
    print("Good")
elif marks>=70 and marks<90:
    print("study more")
else:
    print("lathi charge")

#------------------------------

List = [100, 2, 300, 10, 11, 1000, 2000]
maximum_value = max(List)
print(maximum_value)

#----------------------------
#largetst number
list1 = [10,20,30,50,100,200,500,2000]
largest_number = list1[0]
for i in list1: #iterator
    if i >= largest_number:
        largest_number = i
print(largest_number)


#----------------------------
#smallest number
list1 = [10,20,30,50,100,200,500,2000]
smallest_number = list1[0]
for i in list1:
    if i < smallest_number:
        smallest_number = i
print(smallest_number)

#----------------------------

# creating an empty list
lst = []

# number of elements as input
num = int(input("Enter number of elements : "))

# iterating till the range
for i in range(0, num):
    elements = int(input())

    lst.append(elements)  # adding the element

print(lst)

largest_number = lst[0]
for i in lst: #iterator
    if i >= largest_number:
        largest_number = i
print(largest_number)

