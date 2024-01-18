
def calculate_percentage(total_marks, obtained_marks):
    return (obtained_marks / total_marks) * 100

def calculate_grade(percentage):
    if percentage >= 90:
        return 'A1'
    elif 80 <= percentage < 90:
        return 'A'
    elif 70 <= percentage < 80:
        return 'B'
    elif 60 <= percentage < 70:
        return 'C'
    elif 50 <= percentage < 600:
        return 'D'
    else:
        return 'F'

name = input("Enter your name: ")
father_name = input("Enter your father's name: ")
roll_number = input("Enter your roll number: ")

subjects = []
total_marks = 0

for i in range(5):
    subject_name = input(f"Enter subject {i+1} name: ")
    marks_obtained = int(input(f"Enter marks obtained in {subject_name}: "))
    
    subjects.append((subject_name, marks_obtained))
    total_marks += 100
    
total_obtained_marks = sum(marks for subject, marks in subjects)
percentage = calculate_percentage(total_marks, total_obtained_marks)

grade = calculate_grade(percentage)

print("\nResult:")
print(f"Name: {name}")
print(f"Father's Name: {father_name}")
print(f"Roll Number: {roll_number}")
print("\nSubject-wise Details:")
for subject, marks in subjects:
    print(f"{subject}: {marks}")
print(f"\nTotal Marks: {total_obtained_marks}/{total_marks}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")    