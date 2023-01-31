str='abcd'
lst=[]
a=0
count=0
for i in str:
    lst.append(i)
for i in lst:
    if a<len(lst)-1:
        if lst[a]>lst[a+1]:
            print('false')
            count=1
            break
    a+=1
if count==1:
    lst.sort()
else:
    print('true')