best_students_set = set()
for i in range(5):
    student_name = input(f"Enter the name of the {i+1}st student: ")
    best_students_set.add(student_name)
print("Set of best five students:", best_students_set)

for i in range(2):
    friend_name = input("Enter the name of a friend who left NED: ")
    if friend_name in best_students_set:
        best_students_set.remove(friend_name)
        print(f"{friend_name} has been removed.")
    else:
        print(f"{friend_name} is not in the set.")
print("Updated set of best five students:", best_students_set)
