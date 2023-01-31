'''x=1
assert x>0,
print("x is a positive number")'''

def square(x):
    assert x>=0
    return (x*x)
n=square(2)
print(n) #works
n=square(-2) #error bc negative number
print(n)