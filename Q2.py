import random

student_list = ['Aun', 'Enayat', 'Ahmer', 'Talha', 'Ahmed']
a = []

for i in range(5):
    x = student_list.pop()
    a.append(x)
    if i == 4:
        break

print("Original List:", a)

winning_students = random.sample(a, 2)
print("Scholarship Winners:", winning_students)
remaining_students = set(a) - set(winning_students)
print("Remaining Students:", list(remaining_students))
