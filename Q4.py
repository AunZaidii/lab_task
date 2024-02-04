try:
    with open('nonexistent_file.txt', 'r') as file:
        content = file.read()
        print(content)

except OSError as e:
    print(f"An OSError (IOError) occurred: {e}")

else:
    print("The code inside the try block executed successfully.")

finally:
    print("This block will always be executed, whether an exception occurred or not.")
