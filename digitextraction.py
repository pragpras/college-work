i=int(input('enter a 4 digit integer'))
n=0
while i>=1:
    k=i%10
    print(k)
    n=n+k
    i=i//10
print(n)      