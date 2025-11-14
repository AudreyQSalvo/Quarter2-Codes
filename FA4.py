#Ask user for the number of students and subjects per student
num_students = int(input("Enter number of students: "))
num_subjects = int(input("Enter number of subjects: "))
overall_total = 0

for i in range(1,num_students + 1,1):
    print(f"Student {i}")
    total_score = 0
    #Use a nested loop to let the user input the scores
    for j in range(1,num_subjects + 1,1):
        subj_score = int(input(f"Enter score {j}: "))
        total_score += subj_score
    #Each student’s average
    average = total_score / num_subjects
    print(f"Average for Student {i}: {average}")
    overall_total += average

#The overall class average after all students’ scores are entered
overall_avg =  overall_total / num_students
print(f"Class Average = {overall_avg}")