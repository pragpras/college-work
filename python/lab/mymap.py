#write a function mymap which takes a callback and an iterable, creates a list, applies the callback to each
#element of the iterable and puts the result into list and returns the list. mymap should mimic map
#test this with the following calls:
#a) create a list of square of odd numbers from 1 to n
def odd_sq(a):
    return a**2
def mymap(func,lst):
    result=[]
    for i in lst:
        result.append(func(i))
    return result
n=int(input("enter value for upper range: "))
l=list(mymap(odd_sq,range(1,n,2)))
print(l)

#b) given a list of words, return a list of words with ing appended to it.
def mymap2(func,lst):
    result=[]
    for i in lst:
        result.append(func(i))
    return result
lst=['morn','walk','eat','sleep']
sub='ing'
l=list(mymap(lambda string: string+sub,lst))
print(l)

#c) given a list of words, return a list of tuples having the word and its length
def tuple_str_length(s):
    return s,len(s)
def mymap3(func,lst):
    result=[]
    for i in lst:
        result.append(func(i))
    return result
lst=['morning','walk','eat','sleep']
l=list(mymap(tuple_str_length,lst))
print(l)