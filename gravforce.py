m1=int(input("enter the mass of the first body: "))
m2=int(input("enter the mass of the second body:"))
d=int(input("enter the distance between the bodies: "))
g=6.673*(10**-11)
f=(g*m1*m2)/(d**2)
print("gravitational force= ",f)