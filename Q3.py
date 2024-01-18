lst = [5, 2, 8, 1, 7, 3]

middle_index = len(lst) // 2

middle_element = lst[middle_index]

first_number = lst.pop(0)
lst.append(first_number)


print(f"Index of the middle element: {middle_index}")
print(f"Middle element of lst: {middle_element}")
print(f"Sorted list in descending order: {lst}")
print(f"List after moving the first number to the end:", lst)

