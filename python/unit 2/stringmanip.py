str='pragprasprerpras'
a=str[0:1]
lst=[]
for i in str:
    lst.append(i)
for i in lst:
    if i==a:
        n=lst.index(i)
        lst.remove(i)
        lst.insert(n,'$')
lst.pop(0)
lst.insert(0,a)
s=""
for ele in lst:
    s+=ele
print(s)