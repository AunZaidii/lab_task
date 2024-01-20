def create_guest_list(your_list, parents_list):
    all_guests = your_list + parents_list
    unique_guests = set(all_guests)
    return list(unique_guests)
def compare_guest_lists(your_list, parents_list):
    common_guests = set(your_list).intersection(parents_list)
    return list(common_guests)
def count_guests_with_members(guest_list):
    total_guests = len(guest_list)
    total_members = sum(len(member.split()) for member in guest_list)
    return total_guests, total_members
your_guest_list = [
    'Ahmed',
    'Ali',
    'Sara',
    'Raza',
    'Fatir'
]
parents_guest_list = [
    'Hussain',
    'Naqi',
    'MUjtaba',
    'Zainab',
    'Maryam'
]
all_guests = create_guest_list(your_guest_list, parents_guest_list)
print("Combined Guest List:", all_guests)
common_guests = compare_guest_lists(your_guest_list, parents_guest_list)
print("Common Guests:", common_guests)
total_guests, total_members = count_guests_with_members(all_guests)
print(f"Total Guests: {total_guests}, Total Members: {total_members}")
