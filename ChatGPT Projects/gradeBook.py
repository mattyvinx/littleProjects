studentCount = int(input("Enter the number of students: ")) #ask for how many students in gradebook 

gradebook = {} #initialize gradebook

for i in range (0,studentCount): #iterate through number of students entered 
    name = input(f"Enter the name of student {i+1}: ") #ask for name of current student
    grades = input(f"Enter grades for {name} (comma-separated): ") #ask for grades of student
    str_grades = grades.split(',') #split enterred grades into a list 
    int_grades = [int(x) for x in str_grades] #convert string grades to int 
    gradebook[name]=int_grades #set key of current name to value of int list of grades 

print("Gradebook:")
for j in gradebook:
    print (f"{j}: {gradebook[j]} | Average: {sum(gradebook[j])/len(gradebook[j]):.2f}") #output as requested
