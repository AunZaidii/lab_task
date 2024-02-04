def example_function(index):
    numbers = [1, 2, 3, 4, 5, 6]
    try:
        result = numbers[index]
        division_result = numbers[index] / numbers[index - 1]
        print(f"Element at index {index}: {result}")
        print(f"Division result: {division_result}")
    except IndexError:
        print(f"Error: Index {index} is out of range.")
    except ArithmeticError:
        print(f"Error: Arithmetic error occurred.")
try:
    example_function(5) 
except ArithmeticError:
    print("This exception is caught in the outer try-except block.")
