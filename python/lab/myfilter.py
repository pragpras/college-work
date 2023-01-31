#write a function to mimic filter called myfilter
#test this with the following calls:
#given a list of strings, remove all strings having first character as digit
def myfilter(func,lst):
    result=[]
    for i in lst:
        if func(i):
            result.append(i)
    return result
l=["hi","1gff","h3345","6sds","dfdg","234332"]
print(list(myfilter(lambda x:x if x[0].isdigit()==False else None,l)))