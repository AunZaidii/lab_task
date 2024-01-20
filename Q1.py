sample = [(2, 3), (4, 7), (8, 11), (3, 6)]

element_position = 1
#here will be two element positions 0 and 1
min_value = min(sample, key=lambda x: x[element_position])
max_value = max(sample, key=lambda x: x[element_position])

print(f"Minimum value at position {element_position}:", min_value[element_position])
print(f"Maximum value at position {element_position}:", max_value[element_position])

