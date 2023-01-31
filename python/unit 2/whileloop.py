n=int(input("enter an integer: "))
i=1
while i*i<=n:
    print("square of",i,"is",i*i)
    i+=1
#above program was to display all squares less than or equal to n
#same program with for loop is as follows:
n=int(input("enter an integer: "))
for i in range(1,n):
    if (i*i)<=n:
        print("square of",i,"is",i*i)