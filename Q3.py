try:
    print("This line is indented incorrectly.")
except IndentationError as e:
    print(f"An IndentationError occurred: {e}")
else:
    print("The code inside the try block executed successfully.")
finally:
    print("This block will always be executed, whether an exception occurred or not.")
