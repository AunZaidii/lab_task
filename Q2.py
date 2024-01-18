import os
def Distribution(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()

        grades_list = content.split(" ")
        grade_distribution = {}
        grade_categories = ["A", "A-", "B+", "B", "B-", "C", "C-", "F"]

        for category in grade_categories:
            grade_distribution[category] = grades_list.count(category)

        for grade, count in grade_distribution.items():
            print(f"Number of students who received {grade}: {count}")

    except FileNotFoundError:
        print(f"File '{filename}' not found.")

Distribution("C:\programming1.txt")

