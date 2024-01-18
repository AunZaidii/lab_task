import os
def file_statistics(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()

        line_count = content.count('\n') + 1
        word_count = len(content.split())
        character_count = len(content)

        print(f"Statistics for file '{file_name}':")
        print(f"Line count: {line_count} lines")
        print(f"Word count: {word_count} words")
        print(f"Character count: {character_count} characters")

    except FileNotFoundError:
        print(f"File '{file_name}' not found.")

file_statistics('C:\programming.txt')

