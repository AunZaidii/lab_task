import math
def calculate_ladder_height(length, angle):
    angle_in_radians = math.radians(angle)
    height = length * math.sin(angle_in_radians)
    return height
length_a, angle_a = 16, 75
length_b, angle_b = 20, 0
length_c, angle_c = 24, 45
length_d, angle_d = 24, 80

height_a = calculate_ladder_height(length_a, angle_a)
height_b = calculate_ladder_height(length_b, angle_b)
height_c = calculate_ladder_height(length_c, angle_c)
height_d = calculate_ladder_height(length_d, angle_d)

print(f"Height for (a) 16 feet & 75 degrees: {height_a:.2f} feet")
print(f"Height for (b) 20 feet & 0 degrees: {height_b:.2f} feet")
print(f"Height for (c) 24 feet & 45 degrees: {height_c:.2f} feet")
print(f"Height for (d) 24 feet & 80 degrees: {height_d:.2f} feet")


