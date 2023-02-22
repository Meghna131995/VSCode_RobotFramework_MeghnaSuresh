#formatting strings
a= "My name is Meghna"
b= "how are you"
print("Welcome! " +a)
print("Welcome! {} {}" .format(a,b))
print("Welcome! {1} {0}" .format(a,b))
print("Welcome! {about} {question}" .format(about=a,question=b))