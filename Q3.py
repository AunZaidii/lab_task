def hexASCII():
    lowercase_alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for char in lowercase_alphabet:
        ascii_code = ord(char)
        hex_representation = format(ascii_code, 'x')
        print(f"{char}: {hex_representation}", end=" ")

# Call the function to print the correspondence
hexASCII()
