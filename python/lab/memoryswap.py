x=int(input("enter x"))
y=int(input("enter y"))
z=x
x=y
y=z
print(x)
print(y)
x=int(input("enter new x"))
y=int(input("enter new y"))
x,y=y,x
print(x,y)

