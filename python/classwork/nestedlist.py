class_grades=[[85,91,89],[78,81,86],[62,75,77]]
sum = 0
k = 0
for i in class_grades: #while loop: while k<len(class_grades) works as well
 sum = sum + class_grades[k][0]
 k = k + 1
average_exam1 = sum / float(len(class_grades)) 
print(average_exam1)