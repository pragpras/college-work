n=int(input("enter the number of seconds passed since midnight"))
h=n//3600
m=n%3600
m=m/60
if m>=60:
    h+=1
    m=m-60
print("number of hours passed since midnight",h)
print("number of minutes passed since midnight",m)