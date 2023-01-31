import random
students=[1,2,3,"abc",'d',5]
random.shuffle(students)
print(students)
x=random.choice(students)
print("the class rep is: ",x)
x=random.sample(students,2)
print(x)
a=random.random()
b=random.random()
print(a*b)