import math
dartboard_radius = 10
dart_coordinates = [
    (0, 0),  # (a)
    (10, 10),  # (b)
    (6, 6),  # (c)
    (7, 8)   # (d)
]
for x, y in dart_coordinates:
    is_within_dartboard = math.sqrt(x**2 + y**2) <= dartboard_radius
    print(f"Dart hit at ({x}, {y}) is within the dartboard: {is_within_dartboard}")
