#Dictionary
a={"url1":"https://www.google.com", "url2":"https://www.amazon.in"}
b={1:"Meghna", 2: "Moolya"}
print(b[1])
print(a["url2"])

b[3]="flipkart.com"
print(b)
print(b[3])

print(b.get(1))
print(b.keys())
print(b.items())
print(b.values())

print(b.pop(1))
print(b)
print(b.popitem())
print(b)

b.update({3:"demoqa.com"})
print(b)

b.update({4:"ogangehrm.com", 5:"Meghna"})
print(b)
print(b.keys())

b.setdefault(6,"youtube.com")
print(b)

b.clear()
print(b)