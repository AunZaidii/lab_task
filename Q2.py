class PhoneDirectory:
    def __init__(self):
        self.directory = {}
    def add_member(self, name, phone_number):
        self.directory[name] = phone_number
        print(f"{name} added to the phone directory.")
    def delete_member(self, name):
        if name in self.directory:
            del self.directory[name]
            print(f"{name} deleted from the phone directory.")
        else:
            print(f"{name} not found in the phone directory.")
    def print_directory(self):
        print("\nPhone Directory:")
        for name, phone_number in self.directory.items():
            print(f"{name}: {phone_number}")
        print(f"Total Members: {len(self.directory)}\n")
personal_directory = PhoneDirectory()
personal_directory.add_member("Parent 1", "123-456-7890")
personal_directory.add_member("Parent 2", "987-654-3210")
personal_directory.add_member("Friend 1", "555-123-4567")
personal_directory.add_member("Friend 2", "555-987-6543")
personal_directory.add_member("Friend 3", "555-789-0123")
personal_directory.add_member("Friend 4", "555-456-7890")
personal_directory.add_member("Friend 5", "555-234-5678")
personal_directory.add_member("Friend 6", "555-876-5432")
personal_directory.add_member("Friend 7", "555-345-6789")
personal_directory.add_member("Friend 8", "555-890-1234")
personal_directory.add_member("Friend 9", "555-678-9012")
personal_directory.add_member("Friend 10", "555-012-3456")
personal_directory.print_directory()
personal_directory.delete_member("Friend 5")
personal_directory.print_directory()
